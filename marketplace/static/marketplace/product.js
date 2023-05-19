// document.addEventListener('DOMContentLoaded', function() {
//     console.log("hello")

//     document.getElementById("adding_alert").style.display = 'none';
//     document.getElementById("warning").style.display = 'none';
//     document.getElementById("success").style.display = 'none';
    


//     $('cart_form').on('submit', function(event){
//         event.preventDefault();
//         var prod_id = document.getElementById('prod_id').value;
//         var action = document.getElementById('action').value;
//         add_to_cart(prod_id, action)
//     })

//     function add_to_cart(id, action){
//         console.log("post working")
//         $.ajax({
//             url: `/product/${id}/`,
//             type: 'POST',
//             data: {
//                 action: action,
//                 csrfmiddlewaretoken: $('input[name = csrfmiddlewaretoken]').val(),
//             },
//             async: true,
//             beforeSend: function() {
//                 document.getElementById("adding_alert").style.display = 'block';
//             },
//             success: function(data) {
//                 if (data['message'] === 0) {
//                     document.getElementById("success").style.display = 'block';
//                 }
//                 else if (data['message'] === 1) {
//                     document.getElementById("warning").style.display = 'block';
//                 }
//             },
//             complete: function() {
//                 document.getElementById("adding_alert").style.display = 'none';
//             },
//             error: function(er){
//                 console.log(er)
//             },
//         })
//     }
// });