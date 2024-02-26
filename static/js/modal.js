document.getElementById('loginButton').addEventListener('click', function(e) {
    var myModal = new bootstrap.Modal(document.getElementById('loadingModal'), {});
    myModal.show();
    setTimeout(function() {
        myModal.hide();
    }, 5000);
});
