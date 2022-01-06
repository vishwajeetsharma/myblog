var script = document.createElement('script');
script.type ='text/javascript';
script.src = "https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js";

document.head.appendChild(script);

script.onload = function(){
    tinymce.init({
        selector: '#id_content',
        height:700,
        plugins: 'a11ychecker image advcode charmap casechange export code formatpainter print hr anchor linkchecker autolink link preview wordcount lists checklist media mediaembed fullscreen pageembed permanentpen powerpaste table advtable tinycomments tinymcespellchecker',
      toolbar: 'undo redo | styleselect|fontselect| fontsizeselect | bold italic | alignleft aligncenter alignright alignjustify | ' +
        'bullist numlist outdent indent | link image media | print preview  fullpage | ' +
        'forecolor backcolor emoticons | help | code',
        toolbar_mode: 'wrap',
        tinycomments_mode: 'embedded',
        tinycomments_author: 'Vishwajeet Sharma',

      });
}