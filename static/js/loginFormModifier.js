function changeLabelName(){
    let labelUser = document.querySelector("label[for=id_username]");
    if(labelUser!=undefined){
        labelUser.textContent = 'Benutzer';
    }
    let labelPass = document.querySelector("label[for=id_password]");
    if(labelPass!=undefined){
        labelPass.textContent = 'Passwort';
    }

    let login=document.getElementById("login");
    if(login!=undefined){
        login.value="Anmelden"
    }

    let formSubmit=document.getElementById("displayFormSubmit");
    if(formSubmit!=undefined){
        formSubmit.value="Speichern & Senden"
    }
}
function getYearForCopyRight(){
    let v=new Date().getFullYear();
    document.getElementById("copyRight").innerText="© "+v+ ", MGS | Powered by Rahul ";

}

window.onload = function(){
    changeLabelName();
    getYearForCopyRight();
    calculateSchlepperKm();
    calculateMachineKm();
    document.getElementById("id_OrtDerTankung").disabled = true;
};

function removeError(){
    setTimeout(
        function() {
            document.getElementById("alertDiv").style.display = 'none';
    }, 5000);
}

function removeDiv(){
    setTimeout(
        function() {
            document.getElementById("successDiv").style.display = 'none';
    }, 5000);
}

function dateValidation(){
    console.log(document.getElementById("id_Date").value)
    let date=(document.getElementById("id_Date").value).toString();
    date=date.split("-")
    if(date.length>2){
        let cly=parseInt(date[0]);
        let clm=parseInt(date[1]);
        let cld=parseInt(date[2]);

        let dateObj = new Date();
        let month = dateObj.getUTCMonth() + 1; //months from 1-12
        let day = dateObj.getUTCDate();
        let year = dateObj.getUTCFullYear();
        //Datum darf nicht in der Zukunft liegen oder älter als ein Monat sein!
        let error=false;
        if(cly>year){
            errorid_Date.textContent = "Datum darf nicht in der Zukunft liegen oder älter als ein Monat sein!";
            errorid_Date.style.color = "red";
            error=true;
        }else{
            errorid_Date.textContent = "";
        }

        if(clm>month && error==false){
            errorid_Date.textContent = "Datum darf nicht in der Zukunft liegen oder älter als ein Monat sein!";
            errorid_Date.style.color = "red";
            error=true;
        }else{
            errorid_MaschineStart.textContent = "";
        }

        if(cld>day && error==false){
            errorid_Date.textContent = "Datum darf nicht in der Zukunft liegen oder älter als ein Monat sein!";
            errorid_Date.style.color = "red";
        }else{
            errorid_MaschineStart.textContent = "";
        }
    }
}





window.setTimeout( function() {
    window.location.reload();
  }, 1 * 60 * 1000);