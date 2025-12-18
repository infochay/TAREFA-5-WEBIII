document.addEventListener("DOMContentLoaded", function() {
  const form = document.getElementById("formContato");
  const mensagem = document.getElementById("mensagem");

  form.addEventListener("submit", function(event) {
    let erros = [];

    const nome = document.getElementById("nome").value.trim();
    const email = document.getElementById("email").value.trim();
    const fone = document.getElementById("fone").value.trim();

    // Validação do nome
    if (nome.length < 5 || nome.length > 40) {
      erros.push("O nome deve ter entre 5 e 40 caracteres.");
    }

    // Validação do e-mail
    if (!email.includes("@")) {
      erros.push("O e-mail deve conter '@'.");
    }

    // Validação do telefone (11 números = DDD + celular)
    if (!/^\d{11}$/.test(fone)) {
      erros.push("O telefone deve ter 11 números (DDD + celular).");
    }

    if (erros.length > 0) {
      event.preventDefault();
      mensagem.innerHTML = erros.join("<br>");
    }
  });
});
