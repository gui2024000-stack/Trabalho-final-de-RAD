document.addEventListener("DOMContentLoaded",function(){
    const form=document.getElementById("form-contato");
    const aviso=document.getElementById("aviso");

    if(!form) return;
    form.addEventListener("submit",function(evento){
        aviso.textContent="";
        let erros= [];

        const nome=form.nome.value.trim();
        const email=form.email.value.trim();
        const mensagem=form.mensagem.value.trim();

        if(nome.length<2){
            erros.push("O nome precisa ter pelo menos 2 caracteres.");
        }
        if(!email.includes("@")){
            erros.push("Informe um email válido.");
        }
        if(mensagem.length<5){
            erros.push("A mensagem precisa ter pelo menos 5 caracteres");
        }
        if(erros.length>0){
            evento.preventDefault();
            aviso.textContent=erros.join(" ");
        }
    })
})