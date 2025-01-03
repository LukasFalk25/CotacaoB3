function toggleCotacao(ativoId) {
    var cotacaoDiv = document.getElementById('cotacao-' + ativoId);
    if (cotacaoDiv.style.display === 'none' || cotacaoDiv.style.display === '') {
        cotacaoDiv.style.display = 'block';
    } else {
        cotacaoDiv.style.display = 'none';
    }
}