function verificar(){
    var data = new Date()
    var ano = data.getFullYear()
    var fano = window.document.getElementById('txtano')
    var res = document.querySelector('div#res')
    if(fano.value.length == 0 || fano.value > ano){
        window.alert('[ERRO] Verifique os dados e tente novamente!')
    }else{
        var fsex = window.document.getElementsByName('radsex')
        var idade = ano - Number(fano.value)
        var gênero = ''
        var img = document.createElement('img')
        img.setAttribute('id', 'foto')
        if(fsex[0].checked){
            gênero = 'Masculino'
            if(idade >=0 && idade < 10){
                img.setAttribute('src', 'homemC.png')
            }else if(idade >= 10 && idade < 20){
                img.setAttribute('src', 'homemJ.png')
            }else if(idade >= 20 && idade < 60){
                img.setAttribute('src', 'homemA.png')
            }else{
                img.setAttribute('src', 'homemV.png')
            }
        }else if(fsex[1].checked){
            if(idade >=0 && idade < 10){
                img.setAttribute('src', 'mulherC.png')
            }else if(idade >= 10 && idade < 20){
                img.setAttribute('src', 'mulherJ.png')
            }else if(idade >= 20 && idade < 60){
                img.setAttribute('src', 'mulherA.png')
            }else{
                img.setAttribute('src', 'mulherV.png')
            }
        }
        if(fsex[0].checked) {
            gênero = 'Homem'
        }else if (fsex[1].checked){
            gênero = 'Muher'
        }
        res.style.textAlign = 'center'
        res.innerHTML = `Detectamos ${gênero} com ${idade} anos de idade.`
        res.appendChild(img)
    }
}