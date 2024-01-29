function LabEditBlock(runtime, element) {

    $.ajax({
        type: "GET",
        url: runtime.handlerUrl(element, 'lab'),
        success: function(data) {
          console.log(data)
          if (data.type) {
            const selectElement = document.querySelector('select[name="type-lab"]');
            if (selectElement) {
                [...selectElement.options].forEach(option => {
                    if (option.value === data.type) {
                        option.selected = true;
                    }
                });
            }
        }
        if (data.result.length > 0){
          const textarea = $(element).find('textarea[name=result-lab]')
          textarea.val(data.result); 
        }
    }
    });


    $('.save-button' , element).click(function(event){
        const handlerUrl = runtime.handlerUrl(element, 'lab');
        const value = $(element).find('textarea[name=result-lab]').val()
        const valueSelect = $(element).find('select[name=type-lab]').val();
        console.log(valueSelect)
        const formData = new FormData();
        formData.append('result_lab', value)
        formData.append('type_lab', valueSelect)
        $.ajax({
          type: "POST",
          url: handlerUrl,
          data: formData,
          processData: false,  
          contentType: false, 
          success: function(data) {
        runtime.notify('cancel', {});
        window.location.reload(false);
      }
      });
    })

  
   $('.cancel-button', element).click(function (event){
    runtime.notify('cancel', {});
   })

  }