function mascaraCartao(input) {
    let valor = input.value.replace(/\D/g, ''); // Remove caracteres não numéricos
    valor = valor.replace(/(\d{4})/g, '$1 ').trim(); // Adiciona espaço a cada 4 dígitos
    input.value = valor;
}
document.addEventListener("DOMContentLoaded", function () {
    const inputData = document.getElementById("data");

    function mascaraData(input) {
        let valor = input.value.replace(/\D/g, ''); // Remove caracteres não numéricos
        if (valor.length > 4) valor = valor.slice(0, 4); // Limita a 4 caracteres (MMYY)

        let mes = valor.slice(0, 2);
        let ano = valor.slice(2, 4);

        // Impede que o usuário insira um mês inválido
        if (mes > 12) mes = '12';

        // Adiciona a barra após o mês
        let formatado = mes;
        if (ano) formatado += '/' + ano;

        input.value = formatado;

        // Valida o ano mínimo (25 em diante)
        if (ano.length === 2 && parseInt(ano) < 25) {
            alert("O ano não pode ser menor que 25.");
            input.value = mes + '/25'; // Corrige automaticamente para 25
        }
    }

    inputData.addEventListener("keyup", function () {
        mascaraData(this);
    });
});

