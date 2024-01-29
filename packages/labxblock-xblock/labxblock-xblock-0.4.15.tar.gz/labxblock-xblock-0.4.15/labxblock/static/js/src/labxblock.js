const resize_unit_func = `setTimeout(() => {
  const height = $('#content').prop('scrollHeight')
  const msgData = {
    resize: {
      iframeHeight: height,
      transition: '0s',
    },
    type: 'unit.resize',
  };
  $('.icon-result-summary').toggleClass('active_result');
  $('.detail-lab-result.border-radius-top-left').toggleClass('border-radius-bottom-left');
  window.parent.postMessage(msgData, '*');
}, 10);`

function resize() {
  setTimeout(() => {
    const height = $('#content').prop('scrollHeight')
    const msgData = {
      resize: {
        iframeHeight: height,
        transition: '0s',
      },
      type: 'unit.resize',
    };
    window.parent.postMessage(msgData, '*');
  }, 10);
}


function LabXBlock(runtime, element) {
  console.log('=====================lab================')
  const translations = {
    "Upload a Zip file": {
      en: "Upload a Zip file.",
      vi: "Tải file Zip lên",
    },
    "Compress your project files into a single uncompressed Zip file on your computer limited to 500 MB.":
      {
        en: "Compress your project files into a single uncompressed Zip file on your computer limited to 500 MB.",
        vi: "Nén (các) tệp dự án của bạn thành một tệp zip duy nhất trên máy tính của bạn, giới hạn 500 MB (không nén)",
      },
    "Select file": {
      en: "Select file",
      vi: "Chọn File",
    },
    "Submission date": {
      en: "Submission date",
      vi: "Ngày nộp",
    },
    "Lab content": {
      en: "Lab content",
      vi: "Nội dung bài lab",
    },
    "Reference answers": {
      en: "Reference answers",
      vi: "Đáp án tham khảo",
    },
    "View Lab reference answers": {
      en: "View Lab reference answers",
      vi: "Xem đáp án tham khảo bài Lab",
    },
    "Download submitted lab": {
      en: "Download submitted lab",
      vi: "Tải xuống bài đã nộp",
    },
  };

  function trans(word) {
    const cookieValue = $.cookie("openedx-language-preference");

    return translations[word][cookieValue]
      ? translations[word][cookieValue]
      : translations[word]["en"];
  }

  const usageId = element.getAttribute("data-usage-id");

  function lab_grade() {
    $.ajax({
      type: "POST",
      url: runtime.handlerUrl(element, "increment_count"),
      data: JSON.stringify({ hello: "world" }),
      success: (data) => {},
    });
  }

  $.ajax({
    type: "GET",
    url: runtime.handlerUrl(element, "lab"),
    success: function (data) {
      if (data.block_id == usageId) {
        const labElement = $(element).find("#lab");
        if (data.type === "text") {
          if (!data.result_student) {
            const btnLabText = $(element).find("#btn-lab-text");
            const btnSubmit = $(element).find("#btn-lab-submit");
            btnLabText.removeClass("none");

            $("#btn-lab-text", element).click(function (event) {
              btnSubmit.removeClass("none");
              let newDiv = `
                            <div id='editor'></div>`;
              labElement.append(newDiv);
              ClassicEditor.create(element.querySelector("#editor")).then(
                (editor) => {
                  btnLabText.addClass("none");
                  btnSubmit
                    .click(function (event) {
                      const editorData = editor.getData();
                      const formData = new FormData();
                      formData.append("text", editorData);
                      formData.append("type", "lab");
                      $.ajax({
                        type: "POST",
                        url: runtime.handlerUrl(element, "lab_text"),
                        contentType: false,
                        processData: false,
                        data: formData,
                        success: (data) => {
                          viewResultText(data);
                          lab_grade();
                          resize()
                        },
                      });
                    })
                    .catch((error) => {
                      console.error(error);
                    });
                }
              );
            });
          } else {
            viewResultText(data);
            resize()
          }
        } else if (data.type == "file") {
          $(".lab-text", element).remove();

          // console.log('data', data)
          if (data.url.length == 0) {
            const inputHtml = ` 
                        <div class='notify-upload'>
                            <span> Hãy sử dụng template đã cung cấp để thực hành bài lab của bạn, sau đó lưu lại bài làm của bạn thành một tệp zip duy nhất, giới hạn 500Mb. Nhấn “Chọn file” và nhấn nút “Gửi bài”. </span>
                        </div>
                        <div>
                        <input type="file" name="file" id="file" class="inputfile" accept=".zip"  />      
                        <label class='btn-primary-custom ' for="file"><span>${trans(
                          "Select file"
                        )}</span></label>
                        </div>
                            <div id='file-info'></div>
                        `;
            labElement.append(inputHtml);
            $(element).on("change", ".inputfile", function () {
              const selectedFile = this.files[0];
              // console.log('======upload========', selectedFile)
              const fileInfoContainer = $("#file-info");
              if (selectedFile) {
                fileInfoContainer.html(`
                                   <div class='info-file-content'>
                                    <span><i class="fa fa-file-text file_upload_icon" aria-hidden="true"></i> ${selectedFile.name}</span>
                                    <span style="display: flex;">
                                      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none">
                                        <path d="M12 13.4008L7.10005 18.3008C6.91672 18.4841 6.68338 18.5758 6.40005 18.5758C6.11672 18.5758 5.88338 18.4841 5.70005 18.3008C5.51672 18.1174 5.42505 17.8841 5.42505 17.6008C5.42505 17.3174 5.51672 17.0841 5.70005 16.9008L10.6 12.0008L5.70005 7.10078C5.51672 6.91745 5.42505 6.68411 5.42505 6.40078C5.42505 6.11745 5.51672 5.88411 5.70005 5.70078C5.88338 5.51745 6.11672 5.42578 6.40005 5.42578C6.68338 5.42578 6.91672 5.51745 7.10005 5.70078L12 10.6008L16.9 5.70078C17.0834 5.51745 17.3167 5.42578 17.6 5.42578C17.8834 5.42578 18.1167 5.51745 18.3 5.70078C18.4834 5.88411 18.575 6.11745 18.575 6.40078C18.575 6.68411 18.4834 6.91745 18.3 7.10078L13.4 12.0008L18.3 16.9008C18.4834 17.0841 18.575 17.3174 18.575 17.6008C18.575 17.8841 18.4834 18.1174 18.3 18.3008C18.1167 18.4841 17.8834 18.5758 17.6 18.5758C17.3167 18.5758 17.0834 18.4841 16.9 18.3008L12 13.4008Z" fill="#2C3744"/>
                                      </svg>
                                    
                                    </span>
                                   </div>
                                `);
                $(".inputfile").css("display", "none");
                $('label[for="file"]').css("display", "none");
                $(element).find("#btn-lab-submit").removeClass("none");
                $(element).find(".lab-btn").css("text-align", "start");

                $(".fa-times", element).click(function () {
                  $(".error-message", element).remove();
                  $("#file")[0].value = "";
                  $(".info-file-content", element).remove();

                  $(".inputfile").css("display", "inline-block");
                  $('label[for="file"]').css("display", "inline-block");
                  $(element).find("#btn-lab-submit").addClass("none");
                });
                $(element)
                  .find("#btn-lab-submit")
                  .click(function () {
                    const selectedFile = $("#file")[0].files[0];
                    console.log(
                      "======selectedFile_submit========",
                      selectedFile
                    );
                    if (selectedFile) {
                      const fileSizeInMB = selectedFile.size / (1024 * 1024);
                      const fileType = selectedFile.type;
                      if (fileSizeInMB > 5) {
                        $(".error-message", element).remove();
                        $("#lab").append(
                          '<span class="error-message">File size exceeds 5MB limit</span>'
                        );
                      } else if (
                        fileType !== "application/zip" &&
                        fileType !== "application/x-zip-compressed"
                      ) {
                        // console.log('=====fileType========', fileType)
                        $(".error-message", element).remove();
                        $("#lab").append(
                          '<span class="error-message">File must be a ZIP file</span>'
                        );
                      } else {
                        const formData = new FormData();
                        formData.append("file", selectedFile);
                        formData.append("type", "lab");
                        $.ajax({
                          type: "POST",
                          url: runtime.handlerUrl(element, "upload"),
                          contentType: false,
                          processData: false,
                          data: formData,
                          success: (data) => {
                            $(".error-message", element).remove();
                            lab_grade();
                            viewUpload(data);
                            resize()
                          },
                        });
                      }
                    } else {
                      console.log("No file selected");
                    }
                  });
              } else {
                fileInfoContainer.html("<p>Không có file được chọn.</p>");
              }
            });
          } else {
            viewUpload(data);
            resize()
          }
        }
      }
    },
  });

  function viewDateSuccess(date) {
    let dateObject = new Date(date);
    let year = dateObject.getFullYear();
    let month = dateObject.getMonth() + 1;
    let day = dateObject.getDate();
    let formattedDate = day + " tháng " + month + ", " + year;
    let text = `${trans("Submission date")}: ${formattedDate}`;
    $(".lab-date-success", element).html(text);
    $(".lab-date-success", element).addClass("lab-date ");
  }

  function viewResultText(data) {
    viewDateSuccess(data.date);
    $(".lab-text", element).remove();

    const text = `
            <div>
                <div class='student-lab'>
                    <div class='student-lab-title'>
                        <span>${trans("Lab content")}</span>
                        <span  id='student-lab-edit'>
                            <svg width="17" height="16" viewBox="0 0 17 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path fill-rule="evenodd" clip-rule="evenodd" d="M12.8924 0.165122C13.1554 0.0561096 13.4373 0 13.722 0C14.0067 0 14.2886 0.0561096 14.5516 0.165122C14.8145 0.27409 15.0533 0.433781 15.2545 0.635071L15.8647 1.24535C15.8647 1.24533 15.8648 1.24537 15.8647 1.24535C16.0659 1.44652 16.2256 1.68541 16.3345 1.94826C16.4434 2.21114 16.4995 2.4929 16.4995 2.77745C16.4995 3.06199 16.4434 3.34375 16.3345 3.60663C16.2256 3.86943 16.0661 4.10822 15.8649 4.30936C15.8649 4.30942 15.865 4.3093 15.8649 4.30936L9.68843 10.4891C9.28185 10.8957 8.7302 11.1241 8.15586 11.1241H6.06072C5.68201 11.1241 5.375 10.8171 5.375 10.4383V8.35621C5.37503 7.78201 5.60293 7.23125 6.00866 6.82493L12.1892 0.635421C12.3904 0.434016 12.6295 0.274134 12.8924 0.165122ZM13.722 1.37145C13.6176 1.37145 13.5141 1.39204 13.4176 1.43204C13.3211 1.47203 13.2335 1.53064 13.1597 1.60451C13.1596 1.60454 13.1597 1.60449 13.1597 1.60451L6.97913 7.79398C6.97913 7.79398 6.97913 7.79398 6.97913 7.79398C6.83016 7.94317 6.74647 8.14538 6.74645 8.35621C6.74645 8.35619 6.74645 8.35622 6.74645 8.35621V9.75261H8.15586C8.36652 9.75261 8.56912 9.66883 8.71842 9.5196C8.71837 9.51965 8.71846 9.51956 8.71842 9.5196L14.8949 3.33985C14.9688 3.26603 15.0275 3.17819 15.0675 3.08173C15.1074 2.98526 15.128 2.88186 15.128 2.77745C15.128 2.67303 15.1074 2.56964 15.0675 2.47317C15.0275 2.3767 14.9689 2.28905 14.8951 2.21522L14.2847 1.60483C14.2109 1.53092 14.123 1.47205 14.0264 1.43204C13.9299 1.39204 13.8265 1.37145 13.722 1.37145Z" fill="#2C3744"/>
                            <path fill-rule="evenodd" clip-rule="evenodd" d="M4.57867 1.49923C3.65871 1.6229 3.12864 1.85484 2.74174 2.24174C2.35481 2.62867 2.12289 3.15857 1.99923 4.07838C1.87291 5.01792 1.87145 6.25648 1.87145 8C1.87145 9.74311 1.87291 10.9817 1.99923 11.9213C2.1229 12.8413 2.35484 13.3714 2.74174 13.7583C3.12867 14.1452 3.65857 14.3771 4.57838 14.5008C5.51792 14.6271 6.75648 14.6286 8.5 14.6286C10.2431 14.6286 11.4817 14.6271 12.4213 14.5008C13.3413 14.3771 13.8714 14.1452 14.2583 13.7583C14.6452 13.3713 14.8771 12.8414 15.0008 11.9216C15.1271 10.9821 15.1286 9.74352 15.1286 8C15.1286 7.62128 15.4356 7.31428 15.8143 7.31428C16.193 7.31428 16.5 7.62128 16.5 8V8.05158C16.5 9.73196 16.5 11.0628 16.36 12.1044C16.2159 13.1763 15.9122 14.0438 15.228 14.728C14.5438 15.4123 13.676 15.7159 12.6041 15.86C11.5624 16 10.2316 16 8.55157 16H8.44842C6.76804 16 5.43717 16 4.39563 15.86C3.32372 15.7159 2.45618 15.4122 1.77198 14.728C1.08774 14.0438 0.784115 13.176 0.640006 12.1041C0.499974 11.0624 0.499986 9.73155 0.5 8.05156V7.94841C0.499986 6.26804 0.499974 4.93717 0.640007 3.89563C0.784125 2.82372 1.08778 1.95618 1.77198 1.27198C2.45621 0.587745 3.32399 0.284115 4.39594 0.140006C5.43758 -2.56951e-05 6.76845 -1.4202e-05 8.44844 2.94042e-07L8.5 6.21021e-07C8.87872 6.21021e-07 9.18573 0.30701 9.18573 0.685725C9.18573 1.06444 8.87872 1.37145 8.5 1.37145C6.75689 1.37145 5.51832 1.37291 4.57867 1.49923Z" fill="#2C3744"/>
                            </svg>
                        </span>
                    </div>

                    <div class='student-lab-content'>
                        <span id='content-student-lab'> ${data.result_student}</span>
                    </div>

                </div>


                <div class='result-lab'>
                  <span class='result-lab-title'>${trans("Reference answers")}</span>
                  

                  <div class='result-container'>
                      <span class='result-lab-sub-title'> ${trans("View Lab reference answers")}</span>

                      <details onclick="${resize_unit_func}">
                        
                        <summary class='result-summary icon-result-summary'>
                          <div class="detail-lab-result border-radius-top-left border-radius-bottom-left"  >
                            <span class="detail-lab-result-title">${trans("Reference answers")}</span>
                          </div>
                        </summary>

                        <div class="detail-lab-result border-radius-bottom-left detail-lab-result-content-spc" >
                            <span class="detail-lab-result-content">${data.result}</span>
                        </div>
                        
                      </details>
                        
                  </div>
                </div>
            </div>
        `;
    $(".lab-content", element).html(text);
    $("#lab-notification").removeClass("none");

    // $(element).find('.detail-lab-result').on('toggle', function() {
    //     var $iconSpan = $(element).find('.fa-chevron-right');
    //     if ($(this).prop('open')) {
    //         $iconSpan.hide();
    //     } else {
    //         $iconSpan.show();
    //     }
    // });

    $("#student-lab-edit", element).click(function () {
      $(".student-lab-content", element).addClass("bg-none");
      $("#content-student-lab", element).addClass("none");
      const labElement = $(element).find(".student-lab-content");
      let newDiv = `
            <div id='lab-edit'>
                <div id='editor'>
                    <span>${data.result_student}</span>
                </div>
                <div class='btn-edit'>  
                        
                        <div class="lab-btn ">
                            <span id='lab-huy'  class="btn-primary-custom-outline lab-button" >
                                <span class="text-lab">Huỷ</span>
                            </span>
                        </div>
                        <div class="lab-btn ">
                            <span id='student-edit-submit'  class="btn-primary-custom lab-button"  onclick="${resize_unit_func}">
                                <span class="text-lab">Lưu chỉnh sửa</span>
                            </span>
                        </div>
                 </div>
            </div>
            `;
      labElement.append(newDiv);
      ClassicEditor.create(element.querySelector("#editor")).then((editor) => { 
        $("#lab-huy", element).click(function () {
          $(".student-lab-content", element).removeClass("bg-none");
          $("#content-student-lab", element).removeClass("none");
          $("#lab-edit", element).remove();
        });
        $("#student-edit-submit", element).click(function () {
          $(".student-lab-content", element).removeClass("bg-none");
          const editorData = editor.getData();
          const formData = new FormData();
          formData.append("text", editorData);
          formData.append("type", "lab");

          $.ajax({
            type: "POST",
            url: runtime.handlerUrl(element, "lab_text"),
            contentType: false,
            processData: false,
            data: formData,
            success: (data) => {
              viewResultText(data);
            },
          });
        });
      });
    });
  }

  function viewUpload(data) { // UFC - nơi tạo ra nút download submitted lab
    $(".lab-text", element).remove();
    viewDateSuccess(data.date);
    $(".inputfile").css("display", "none");
    $('label[for="file"]').css("display", "none");
    $(".notify-upload").css("display", "none");
    const text = `
        <div>
            <div class='student-lab' style="display:none;">
                <div style='padding:10px 0px;' >
                    <a class='btn-primary-custom-outline student-file'  href=${
                      data.url
                    } target='_blank' > 
                        <span>${trans("Download submitted lab")} </span>
                    </a>
                </div>
            </div>

            <div class='result-lab'>
                <span class='result-lab-title' >${trans("Reference answers")}</span>
                
                
                
                <div class='result-container'> 
                  <span class='result-lab-sub-title'> ${trans("View Lab reference answers")}</span>
                
                  <details onclick="${resize_unit_func}">
                    
                    <summary class='result-summary icon-result-summary'>
                      <div class="detail-lab-result border-radius-top-left border-radius-bottom-left">
                        <span class="detail-lab-result-title">${trans("Reference answers")}</span>
                      </div>
                    </summary>

                    <div class="detail-lab-result border-radius-bottom-left detail-lab-result-content-spc" >
                      <span class="detail-lab-result-content">${data.result}</span>
                    </div>
                      
                  </details>
                  
                </div>


            </div>
        </div>
    `;

    const download_link = `
          <a class='' href=${data.url} target='_blank' > 
              <span>${trans("Download submitted lab")} </span>
          </a>
    `;
  



    $(".lab-content", element).html(text);
    $("#lab-notification").removeClass("none");

    // show download button vetical with notification lab
    $(".btn_download_submitted_lab", element).html(download_link);
    

    // $(element).find('.detail-lab-result').on('toggle', function() {
    //     var $iconSpan = $(element).find('.fa-chevron-right');
    //     if ($(this).prop('open')) {
    //         $iconSpan.hide();
    //     } else {
    //         $iconSpan.show();
    //     }
    // })
  }
}
