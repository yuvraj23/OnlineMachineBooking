var regExp = /[a-zA-Z]/g;
function calculateSchlepperKm(){
    document.getElementById("alertDiv").style.display = 'none';
    let dropdownList= document.getElementById('id_Schlepper');
    if(dropdownList.value=="Kein Schlepper" || dropdownList.value=="None" ){
            disableSchlepper();
            document.getElementById("id_OrtDerTankung").disabled = true;
            document.getElementById("id_LiterDiesel").value="0";
            document.getElementById("id_LiterDiesel").readOnly=true;
    }else{
            document.getElementById("id_OrtDerTankung").disabled = false;
            let input1 = document.getElementById("id_SchlepperLastRecord");
            input1.readOnly = true;

            let input2 = document.getElementById("id_SchlepperStart");
            input2.readOnly = true;

            let input3= document.getElementById("id_SchlepperEnde");
            input3.readOnly = false;

            let input4 = document.getElementById("id_SchlepperAnzahl");
            input4.readOnly = true;

            if(dropdownList!=null){

                if(sdata.get(dropdownList.value)!=null){

                   let inputE = document.getElementById("id_SchlepperLastRecord");
                    inputE.value = sdata.get(dropdownList.value);
                    let inputF = document.getElementById("id_SchlepperStart");
                    inputF.value = sdata.get(dropdownList.value);
                }
            }
        }
}

function disableSchlepper(){

    document.getElementById("id_SchlepperLastRecord").value=0;
    document.getElementById("id_SchlepperLastRecord").readOnly=true;

    document.getElementById("id_SchlepperStart").value=0;
    document.getElementById("id_SchlepperStart").readOnly=true;


   document.getElementById("id_SchlepperEnde").value=0;
   document.getElementById("id_SchlepperEnde").readOnly=true;


    document.getElementById("id_SchlepperAnzahl").value=0;
    document.getElementById("id_SchlepperAnzahl").readOnly=true;

}


function setSchlepperValue(d){

     let result = d.substring(1, d.length-1);
     let myArray = result.split(",");
     var sdata = new Map();
     for (var i = 0; i < myArray.length; i++) {
        let arr=myArray[i].split(":")
        let key=arr[0];
        key=key.substring(1,key.length-1);
        let val=arr[1].trim()+"";
        key=key.replaceAll("'","").replaceAll('"',"")
        val=val.replaceAll("'","").replaceAll('"',"")
        sdata.set(key,val);
    }
    globalThis.sdata =sdata;
}

function setSchlepperUnit(d){

    let result = d.substring(1, d.length-1);
    let myArray = result.split(",");
    var schlepperUnit = new Map();
    for (var i = 0; i < myArray.length; i++) {
       let arr=myArray[i].split(":")
       let key=arr[0];
       key=key.substring(1,key.length-1);
       let val=arr[1].trim()+"";
       key=key.replaceAll("'","").replaceAll('"',"")
       val=val.replaceAll("'","").replaceAll('"',"")
       schlepperUnit.set(key,val);
   }
   globalThis.schlepperUnit =schlepperUnit;
}

function getEndSchlepperVal(){
    var inputF = document.getElementById("id_SchlepperLastRecord");
    var x = document.getElementById("id_SchlepperEnde").value;
    let dropdownList = document.getElementById('id_Schlepper');
    let y= sdata.get(dropdownList.value);
    inputF.value = (parseInt(x)+parseInt(y)).toString();
}

function validatestartSchlepperValue(){
     // Changing content and color of content
     let invalid=false;
     if(Number.isInteger(document.getElementById("id_SchlepperLastRecord").value.trim()) || regExp.test(document.getElementById("id_SchlepperLastRecord").value.trim())){
        invalid=true;
     }
     if(Number.isInteger(document.getElementById("id_SchlepperStart").value.trim())){
        invalid=true;
     }

     if(invalid==false){
        let x=parseInt(document.getElementById("id_SchlepperLastRecord").value.trim())
        let y=parseInt(document.getElementById("id_SchlepperStart").value.trim())
        if(x<y){
            errorid_SchlepperStart.textContent = "Bitte geben Sie einen gültigen Wert ein. - "+document.getElementById("id_SchlepperLastRecord").value
            errorid_SchlepperStart.style.color = "red"
        }else{
            errorid_id_SchlepperStart.textContent = ""
        }
     }
}

function validateEndSchlepperValue(){
    // Changing content and color of content
    let x=parseInt(document.getElementById("id_SchlepperEnde").value);
    let y=parseInt(document.getElementById("id_SchlepperStart").value);
    val=true;
    if(!Number.isInteger(x) || regExp.test(x)){
        errorid_SchlepperEnde.textContent = "der Wert darf nicht kleiner als das Feld *Anfang* sein";
       errorid_SchlepperEnde.style.color = "red";
       val=false;
    }

    if(!Number.isInteger(y) || regExp.test(y)){
        errorid_SchlepperEnde.textContent = "der Wert darf nicht kleiner als das Feld *Anfang* sein";
       errorid_SchlepperEnde.style.color = "red";
       val=false;
    }

    if(val){
         x=parseFloat(x);
        y=parseFloat(y);
        if(x<y){
            errorid_SchlepperEnde.textContent = "Bitte geben Sie einen gültigen Wert ein. - "+document.getElementById("id_SchlepperLastRecord").value;
            errorid_SchlepperEnde.style.color = "red";
         }else{
             errorid_SchlepperEnde.textContent = "";
         }
    }

}

function calculateSchlepperDiff(){

    let x=parseFloat(document.getElementById("id_SchlepperStart").value).toFixed(2)
    let y=parseFloat(document.getElementById("id_SchlepperEnde").value).toFixed(2)
    if(y==NaN){
        errorid_SchlepperEnde.textContent = "der Wert darf nicht kleiner als das Feld *Anfang* sein"
        errorid_SchlepperEnde.style.color = "red"
    }
    if(x==NaN){
        errorid_SchlepperStart.textContent = "der Wert darf nicht kleiner als das Feld *Anfang* sein"
        errorid_SchlepperStart.style.color = "red"
    }
    let diff=parseFloat(Number(y).toFixed(2) - Number(x).toFixed(2)).toFixed(2)
    let dc=countDecimals(diff);
    let unit=setSchlUnit();
    if(unit!='ha' && unit!='Std'){
        x=parseInt(x);
        y=parseInt(y);
        diff=parseInt(diff);
    }
    if(y<x || (x==y && dc=="00")){
        errorid_SchlepperEnde.textContent = "der Wert darf nicht kleiner als das Feld *Anfang* sein"
        errorid_SchlepperEnde.style.color = "red"
     }else{
        let inputF = document.getElementById("id_SchlepperAnzahl");
        inputF.value =(diff).toString();

     }
}

function countDecimals(num)
{
    // Convert to String
   const numStr = String(num);
   // String Contains Decimal
   if (numStr.includes('.')) {
      return numStr.split('.')[1];
   };
   // String Does Not Contain Decimal
   return 0;
}

function fnValidate(){

    let dropdownList1 = document.getElementById('id_Auftragsgeber');
    let dropdownList2 = document.getElementById('id_Betrieb');
    let dropdownList3 = document.getElementById('id_Fahrer');
    let dropdownList4 = document.getElementById('id_Schlepper');
    let dropdownList5 = document.getElementById('id_Maschine');
    let dropdownList6 = document.getElementById('id_Taetigkeit');
    let dropdownList7 = document.getElementById('id_OrtDerTankung');
    let lst=[];
    let valid = true;
    let valNotize=document.getElementById("id_Notizen").value;
    if(valNotize==""){
        document.getElementById("id_Notizen").value="None";
    }

    if(dropdownList1.value=="" || dropdownList1.value=="None"){
        errorid_Auftragsgeber.textContent = "Bitte geben Sie einen gültigen Wert ein "
        errorid_Auftragsgeber.style.color = "red"
       valid=false;
       lst.push("id_Auftragsgeber");
    }else{
        errorid_Auftragsgeber.textContent = ""
    }
    /*if(dropdownList2.value=="" || dropdownList2.value=="None"){
        errorid_Betrieb.textContent = "Bitte geben Sie einen gültigen Wert ein"
       errorid_Betrieb.style.color = "red"
       valid=false;
    }else{
        errorid_Betrieb.textContent = ""
    }
    if(dropdownList3.value=="" || dropdownList3.value=="None"){
        errorid_Fahrer.textContent = "Bitte geben Sie einen gültigen Wert ein"
       errorid_Fahrer.style.color = "red"
       valid=false;
    }else{
        errorid_Fahrer.textContent = ""
    }*/
    if(dropdownList4.value==""){
        errorid_Schlepper.textContent = "Bitte geben Sie einen gültigen Wert ein"
       errorid_Schlepper.style.color = "red"
       valid=false;
       lst.push("id_Schlepper");
    }else{
        errorid_Schlepper.textContent = ""
    }
    if(dropdownList5.value==""){
        errorid_Maschine.textContent = "Bitte geben Sie einen gültigen Wert ein"
       errorid_Maschine.style.color = "red"
       valid=false;
       lst.push("id_Maschine");
    }else{
        errorid_Maschine.textContent = ""
    }
    /*if(dropdownList6.value=="" || dropdownList6.value=="None"){
        errorid_Taetigkeit.textContent = "Bitte geben Sie einen gültigen Wert ein"
       errorid_Taetigkeit.style.color = "red"
       valid=false;
    }else{
        errorid_Taetigkeit.textContent = ""
    }*/

    if(dropdownList4.value!="Kein Schlepper" && dropdownList4.value!="None"){
        if(dropdownList7.value=="" || dropdownList7.value=="None"){
            errorid_OrtDerTankung.textContent = "Bitte geben Sie einen gültigen Wert ein"
           errorid_OrtDerTankung.style.color = "red"
           valid=false;
           lst.push("id_OrtDerTankung");
        }else{
            errorid_OrtDerTankung.textContent = ""
        }

        if(dropdownList7.value=="Halle"){
            let vl=document.getElementById("id_LiterDiesel").value;
            if(vl=="None" || vl.trim()=="" || vl.trim()=="0"){
                errorid_LiterDiesel.textContent = "Bitte geben Sie einen gültigen Wert ein"
                errorid_LiterDiesel.style.color = "red"
                valid=false;
                lst.push("id_LiterDiesel");
            }else{
                errorid_LiterDiesel.textContent = ""
            }
            let va1=integerCheck();
            if(va1==false){
                valid=false;
            }
        }
    }

    let count=0;
    if(dropdownList4.value!="Kein Schlepper"){
        let v1 = document.getElementById("id_SchlepperLastRecord").value;
        if(v1=="" || v1=="None"){
            errorid_SchlepperLastRecord.textContent = "Bitte geben Sie einen gültigen Wert ein"
           errorid_SchlepperLastRecord.style.color = "red"
           valid=false;
           lst.push("id_SchlepperLastRecord");
        }else{
            errorid_SchlepperLastRecord.textContent = ""
        }
        let v2 = document.getElementById("id_SchlepperStart").value;
        if(v2=="" || v2=="None"){
            errorid_SchlepperStart.textContent = "Bitte geben Sie einen gültigen Wert ein"
           errorid_SchlepperStart.style.color = "red"
           valid=false;
           lst.push("id_SchlepperStart");
        }else{
            errorid_SchlepperStart.textContent = ""
        }
        let v3 = document.getElementById("id_SchlepperEnde").value;
        if(v3=="" || v3=="None" || v3=="0"){
            errorid_SchlepperEnde.textContent = "Bitte geben Sie einen gültigen Wert ein"
           errorid_SchlepperEnde.style.color = "red"
           valid=false;
           lst.push("id_SchlepperEnde");
        }else{
            errorid_SchlepperEnde.textContent = ""
        }
        let v4 = document.getElementById("id_SchlepperAnzahl").value;
        if(v4=="" || v4=="None"){
            errorid_SchlepperAnzahl.textContent = "Bitte geben Sie einen gültigen Wert ein"
           errorid_SchlepperAnzahl.style.color = "red"
           valid=false;
           lst.push("id_SchlepperAnzahl");
        }else{
            errorid_SchlepperAnzahl.textContent = ""
        }
    }else{
        count++;
    }

    if(dropdownList5.value!="Keine Maschine" && !disableMachineField.has(dropdownList5.value)){
        let v5 = document.getElementById("id_MaschineLastRecord").value;
        if(v5=="" || v5=="None"){
            errorid_MaschineLastRecord.textContent = "Bitte geben Sie einen gültigen Wert ein"
        errorid_MaschineLastRecord.style.color = "red"
        valid=false;
        lst.push("id_MaschineLastRecord");
        }else{
            errorid_MaschineLastRecord.textContent = ""
        }
        let v6 = document.getElementById("id_MaschineStart").value;
        if(v6=="" || v6=="None"){
            errorid_MaschineStart.textContent = "Bitte geben Sie einen gültigen Wert ein"
        errorid_MaschineStart.style.color = "red"
        valid=false;
        lst.push("id_MaschineStart");
        }else{
            errorid_MaschineStart.textContent = ""
        }
        let v7 = document.getElementById("id_MaschineEnde").value;
        if(v7=="" || v7=="None" || v7=="0"){
            errorid_MaschineEnde.textContent = "Bitte geben Sie einen gültigen Wert ein"
        errorid_MaschineEnde.style.color = "red"
        valid=false;
        lst.push("id_MaschineEnde");
        }else{
            errorid_MaschineEnde.textContent = ""
        }
        let v8 = document.getElementById("id_MaschineAnzahl").value;
        if(v8=="" || v8=="None"){
            errorid_MaschineAnzahl.textContent = "Bitte geben Sie einen gültigen Wert ein"
        errorid_MaschineAnzahl.style.color = "red"
        valid=false;
        lst.push("id_MaschineAnzahl");
        }else{
            errorid_MaschineAnzahl.textContent = ""
        }

    }else{
        if( !disableMachineField.has(dropdownList5.value)){
            count++;
        }

    }

    if(count==2){
        document.getElementById("alertDiv").style.display = 'flex';
        setTimeout(
            function() {
                document.getElementById("alertDiv").style.display = 'none';
            }, 500000);
        valid=false;
    }
    let va=blockField("id_Notizen")

    if(va==false){
        valid=false;
    }
    if(valid==false){
       if(valNotize=="None" || valNotize==""){
            document.getElementById("id_Notizen").value="";
        }
    }

    if(valid==false){
        document.getElementById("errorSubmitMsg").style.display = 'flex';
        setTimeout(
            function() {
                document.getElementById("errorSubmitMsg").style.display = 'none';
            }, 50000);
            document.getElementById("displayFormSubmit").style.backgroundColor="Red";
            $(document).scrollTop(0);
        valid=false;
    }else{
        document.getElementById("errorSubmitMsg").style.display = 'none';
        document.getElementById("displayFormSubmit").style.backgroundColor="Green";
    }

    if(valid==true){
        $("#my_form :disabled").removeAttr('disabled');
    }

    return valid;

}

$('#my_form').submit(function(){
    $("#my_form :disabled").removeAttr('disabled');
});

function integerCheck(){
    let input= document.getElementById("id_LiterDiesel").value;
    valid=true;
    if(!Number.isInteger(parseInt(input)) || regExp.test(input)){
        errorid_LiterDiesel.textContent = "keine buchstaben!nur zahlen eingabe möglich!";
        errorid_LiterDiesel.style.color = "red";
        error=true;
        setTimeout(
            function() {
                errorid_LiterDiesel.textContent ="";
            }, 5000);
        valid=false;
    }
    return valid;
}


function setSchlUnit(){
    let dropdownList = document.getElementById('id_Schlepper');
    let y= schlepperUnit.get(dropdownList.value);
    if (y==undefined){
        y="---"
    }
    document.getElementById("unitid_SchlepperLastRecord").textContent=y;
     return y;

}

function blockField(id){
    let valid=true
    if(id=="id_OrtDerTankung"){
        let val=document.getElementById("id_OrtDerTankung").value;
        if(val=="Eigen" || val=="None"){
            document.getElementById("id_LiterDiesel").value="0";
            document.getElementById('id_LiterDiesel').readOnly=true;
        }else{
             document.getElementById("id_LiterDiesel").value="0";
            document.getElementById('id_LiterDiesel').readOnly=false;
        }
    }

    if(id="id_Notizen"){
        let val1=document.getElementById("id_Betrieb").value;
        let val2=document.getElementById("id_Fahrer").value;
        let val3=document.getElementById("id_Taetigkeit").value;
        let val4 = document.getElementById('id_Auftragsgeber').value;
        let msg="";
        let isNeu=false;

        if(val1=='neu'){

            isNeu=true;
            msg=msg+", "+"Betrieb";
        }
        if(val2=='neu'){

            isNeu=true;
            msg=msg+", "+"Fahrer";
        }
        if(val3=='neu'){

            isNeu=true;
            msg=msg+", "+"Taetigkeit";
        }
        if(val4=='neu'){
            isNeu=true;
            msg=msg+", "+"Auftragsgeber";
        }
        if(isNeu==true){
            let val4=document.getElementById("id_Notizen").value;
            if(val4=="None" || val4=="None"){
                valid=false;
                errorid_Notizen.textContent ="Falls Sie oben *neu* ausgewählt haben, bitte hier Notiz schreiben."+msg
                errorid_Notizen.style.color = "red"
            }else{
                valid=true;
            }

        }
    }

    return valid;
}







