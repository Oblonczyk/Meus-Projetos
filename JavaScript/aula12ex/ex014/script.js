function carregar() {

    var msg = window.document.getElementById('msg')
    var img = window.document.getElementById('imagem')
    var data = new Date()
    var hora = data.getHours()
    var minuto = data.getMinutes()
    msg.innerText = `Agora são ${hora} horas e ${minuto} minutos.`

    if (hora >= 0 && hora < 12){
        //Bom dia
        img.src = 'imgDia.png'
        document.body.style.background = '#e2cd9f'
    }else if (hora >= 12 && hora < 18){
        //Boa tarde
        img.src = 'imgTarde.png'
        document.body.style.background = '#b9846f'
    }else{
        //Boa noite
        img.src = 'imgNoite.png'
        document.body.style.background = '515154'
    }
}