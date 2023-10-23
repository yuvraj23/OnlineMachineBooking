
function calculateMachineKm(){
    let dropdownList= document.getElementById('id_Maschine');
    document.getElementById("alertDiv").style.display = 'none';
    if(dropdownList.value=="Keine Maschine" || dropdownList.value=="None"){
            disableMachine();
    }else{
                let input1 = document.getElementById("id_MaschineLastRecord");
                input1.readOnly = true;

                let input2 = document.getElementById("id_MaschineStart");
                input2.readOnly = true;

                let input3= document.getElementById("id_MaschineEnde");
                input3.readOnly = false;

                let input4 = document.getElementById("id_MaschineAnzahl");
                input4.readOnly = true;

        let dropdownList = document.getElementById('id_Maschine');
        if(disableMachineField.has(dropdownList.value)){
            input3.readOnly = true;
            input4.readOnly = false;
              document.getElementById("id_MaschineLastRecord").value="0";
            document.getElementById("id_MaschineEnde").value="0";
            document.getElementById("id_MaschineStart").value="0";
            return;
        }
        if(dropdownList!=null){

            if(data.get(dropdownList.value)!=null){

                var inputE = document.getElementById("id_MaschineLastRecord");
                inputE.value = data.get(dropdownList.value);

                var inputF = document.getElementById("id_MaschineStart");
                inputF.value = data.get(dropdownList.value);
            }
        }
    }
}

function disableMachine(){

    document.getElementById("id_MaschineLastRecord").value=0;
    document.getElementById("id_MaschineLastRecord").readOnly=true;

    document.getElementById("id_MaschineStart").value=0;
    document.getElementById("id_MaschineStart").readOnly=true;


   document.getElementById("id_MaschineEnde").value=0;
   document.getElementById("id_MaschineEnde").readOnly=true;


    document.getElementById("id_MaschineAnzahl").value=0;
    document.getElementById("id_MaschineAnzahl").readOnly=true;

}



function setMachineValue(d){

   //  globalThis.data = JSON.parse(d);
     let result = d.substring(1, d.length-1);
     let myArray = result.split(",");
     var data = new Map();
     for (var i = 0; i < myArray.length; i++) {
        let arr=myArray[i].split(":")
        let key=arr[0];
        key=key.substring(2,key.length-1);
        let val=arr[1].trim()+"";
        data.set(key,val);

    }
    globalThis.data =data;
}

function setMachineUnit(d){
    let result = d.substring(1, d.length-1);
    let myArray = result.split(",");
    var machineUnit = new Map();
    for (var i = 0; i < myArray.length; i++) {
       let arr=myArray[i].split(":")
       let key=arr[0];
       key=key.substring(1,key.length-1);
       let val=arr[1].trim()+"";
       key=key.replaceAll("'","").replaceAll('"',"")
       val=val.replaceAll("'","").replaceAll('"',"")
       machineUnit.set(key,val);
   }
   globalThis.machineUnit =machineUnit;
}


function getEndMachineVal(){
    var inputF = document.getElementById("id_MaschineLastRecord");
    var x = document.getElementById("id_MaschineEnde").value;
    let dropdownList = document.getElementById('id_Maschine');
    let y= data.get(dropdownList.value);
    inputF.value = (parseInt(x)+parseInt(y)).toString();
}

function setMachineToDisableFields(d){

    //  globalThis.data = JSON.parse(d);
      let result = d.substring(1, d.length-1);
      let myArray = d.split(",");
      let data = new Map();
      for (var i = 0; i < myArray.length; i++) {
         let arr=myArray[i].split(":")
         let key=arr[0];
         key=key.substring(2,key.length-1);
         let val=arr[1].trim()+"";
         data.set(key,val);

     }
     globalThis.disableMachineField =data;
 }


function validateStartValue(){
     // Changing content and color of content
     let x=parseInt(document.getElementById("id_MaschineLastRecord").value)
     let y=parseInt(document.getElementById("id_MaschineStart").value)
     if(y<x){
        errorid_MaschineStart.textContent = "Bitte geben Sie einen gültigen Wert ein. "+document.getElementById("id_MaschineLastRecord").value
        errorid_MaschineStart.style.color = "red"
     }else{
        errorid_MaschineStart.textContent = ""
     }
}

function validateEndValue(){
    // Changing content and color of content
    let x=parseInt(document.getElementById("id_MaschineEnde").value)
    let y=parseInt(document.getElementById("id_MaschineStart").value)
    val=true;
    if(!Number.isInteger(x) || regExp.test(x)){
        errorid_MaschineEnde.textContent = "keine buchstaben!nur zahlen eingabe möglich.!";
       errorid_MaschineEnde.style.color = "red";
       val=false;
    }

    if(!Number.isInteger(y) || regExp.test(y)){
        errorid_MaschineStart.textContent = "keine buchstaben!nur zahlen eingabe möglich.!";
       errorid_MaschineStart.style.color = "red";
       val=false;
    }
    if(val){
         x=parseFloat(x);
        y=parseFloat(y);
        if(x<y){
            errorid_MaschineEnde.textContent = "Bitte geben Sie einen gültigen Wert ein. "+document.getElementById("id_MaschineLastRecord").value
            errorid_MaschineEnde.style.color = "red"
         }else{
            errorid_MaschineEnde.textContent = ""
         }
    }

}

function calculateDiff(){

    let x=parseFloat(document.getElementById("id_MaschineStart").value).toFixed(2)
    let y=parseFloat(document.getElementById("id_MaschineEnde").value).toFixed(2)
    x=parseFloat(x)
    y=parseFloat(y)
    let val=true;

    if(y==NaN){
        errorid_SchlepperEnde.textContent = "der Wert darf nicht kleiner als das Feld *Anfang* sein"
        errorid_SchlepperEnde.style.color = "red";
        val=false;
    }
    if(x==NaN){
        errorid_SchlepperStart.textContent = "der Wert darf nicht kleiner als das Feld *Anfang* sein"
        errorid_SchlepperStart.style.color = "red"
        val=false
    }
    if(val){
        let diff=parseFloat(Number(y).toFixed(2) - Number(x).toFixed(2)).toFixed(2);
         let dc=countDecimals(diff);
        let unit=setMachUnit();
        if(unit!='ha' && unit!='Std'){
            x=parseInt(x);
            y=parseInt(y);
            diff=parseInt(diff);
        }

        if(y<x || (x==y && dc=="00")){
            errorid_MaschineEnde.textContent = "der Wert darf nicht kleiner als das Feld *Anfang* sein"
            errorid_MaschineEnde.style.color = "red"
         }else{
            errorid_MaschineEnde.textContent = ""
            var inputF = document.getElementById("id_MaschineAnzahl");
            inputF.value =(diff).toString();

         }
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


function over(id){

    let v=document.getElementById(id).value;
    if(v.length==0){
        document.getElementById("valid"+id).style.display = 'flex';
        setTimeout(
            function() {
                document.getElementById("valid"+id).style.display = 'none';
            }, 5000);
     }else{
        document.getElementById("valid"+id).style.display = 'none';
     }
}

function out(id){
    document.getElementById("valid"+id).style.display = 'none';
}



function setMachUnit(){
    let dropdownList = document.getElementById('id_Maschine');
    let y= machineUnit.get(dropdownList.value.trim());
    if (y==undefined){
        y="-----"
    }
    document.getElementById("unitid_MaschineLastRecord").textContent=y;
    return y;

}



