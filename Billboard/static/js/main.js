$('document').ready(function(){
   $('.post-new-cont').hide();
   $('.create-new-cont.font-cont').hide();

    $(".btn.btn-add").click(function(){
    //console.log("'+' button")
    $('.btn.btn-add').hide();
    $('.create-new-cont.font-cont').show();
    $('.post-new-cont').show();
        });

    $(".btn.btn-times") .click(function(){
      //console.log("'x' button ")
        $('.post-new-cont').hide();
        $('.create-new-cont.font-cont').hide();
        $('.btn.btn-add').show();
    });
});