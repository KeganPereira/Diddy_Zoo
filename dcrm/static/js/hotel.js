function update_cost(){ 

let arrive = document.getElementId('id_hotel_booking_date_arrive').value 
let leave = document.getElementById('id_hotel_booking_date_leave').value

arrive= new Date(arrive)  
leave= new Date(leave) 
diff= leave.getTime()- arrive.getTime(); 
days = Math.round(Math.abs(diff/(1000*60*60*24))); 

if(String(days) == "NaN"){ 
   let price = document.getElementById('hotel_output') 
   price.innerHTML= "Hotel cost: Date has been chosen" 


} else{ 

    let total=parseInt(adult.value)*65 
               +parseInt(children.value)*35 
               +parseInt(oaps.value)*45  


            
    total = total* days 






    let price = document.getElementId('hotel_output') 

    price.innerHTML= "Hotel cost: £"+ String(total)  



    let adults = document.getElementId("id_hotel_booking_adult"); 
    adults.addEventListener("change", update_cost) 
    let children= document.getElementById("id_hotel_booking_children"); 
    children.addEventListener("change", update_cost) 
    let oaps= document.getElementById("id_hotel_booking_oap"); 
    oaps.addEventListener("change", update_cost)  

    // TO OD: add the same update for the fields




}

}