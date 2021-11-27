
$("#btnsubmit").click(function(){

    let titleid = $("#titleid").val();
    let descriptionid = $("#descriptionid").val();
    let technologyid = $("#technologyid").val();
    let collaboratorid = $("#collaboratorid").val();
    let statusid = $("#statusid").val();
    let csrToken = $("input[name=csrfmiddlewaretoken]").val();

    context = 
    { 
        title: titleid, 
        description:descriptionid, 
        technology:technologyid, 
        collaborator:collaboratorid, 
        status:statusid,
        csrfmiddlewaretoken:csrToken
    };
   $.ajax({
       url: "project_create/",
       method: "POST",
       data: context,
       dataType: "json",
       success: function(data){
           $("form")[0].reset();
       }
   });

});
