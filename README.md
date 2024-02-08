
**#Partner Nofication Project#**

     * The ability of independent online systems to communicate with one 
       another and share transaction data to the customer *
       
     * This provides a way for one system (the source) to "speak" (HTTP request) to customer url (the destination) when an event occurs, and share information (request payload) about 
       the event that occurred.
    
     * this project is  to notify customer for the transaction to be perform
  
     * It created with python programming language 
   
     * The project is two python class server and webhook it notify the transaction detail to the partner from the server 
     
     * it tested to local machine (127.0.0.1:5000\webhook) and to the https:\\webhook.site with json format.
       
****Requests****

     this project is used webhook is an HTTP and HTTPS request, triggered by an event in a payement notfication system and sent to a destination system URL 
    
****JSON****

     for sending content type file format 

***Post Method***

     test result 

***Raw Content***

{

    "id": "1dd2854e-3a79-4548-ae36-97e4a18ebf81",
     
      "amount": 100,
     
      "currency": "ETB",
  
      "created_at_time": 1673381836,
  
      "timestamp": 1701272333,
  
      "cause": "Testing",
  
      "full_name": "Abebe Kebede",
  
      "account_name": "abebekebede1",
  
      "invoice_url": "https://yayawallet.com/en/invoice/xxxx"
  
}



