// Sending Resume to Organization
$(document).ready(function(){
    $("#search-org").click(function(){
        let fileName = $("#resume-name")[0].value.replace("C:\\fakepath\\", "").replace(".docx", "");
        this.href = "orgnization/" + fileName + "/";
    });
});

// Sending Resume to Question
$(document).ready(function(){
    $("#search-question").click(function(){
        let fileName = $("#resume-name")[0].value.replace("C:\\fakepath\\", "").replace(".docx", "");
        this.href = "question/" + fileName + "/";
    });
});