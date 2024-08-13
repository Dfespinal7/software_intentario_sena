function actdocumento(){
    var documento=document.getElementById('documento');
    var selectedOption = documento.options[documento.selectedIndex];
    var valor = selectedOption.getAttribute('data-documento');
    document.getElementById('doc').value = valor;
}
