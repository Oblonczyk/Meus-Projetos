function contar(){
    let ini = document.getElementById('txti')
    let fim = document.getElementById('txtf')
    let pas = document.getElementById('txtp')
    let res = document.getElementById('res')
    if (ini.value.length == 0 || fim.value.length == 0 || pas.value.length == 0) {
        window.alert('[ERRO] FALTAM DADOS')
    }else{
        res.innerHTML = 'CONTANDO: '
        let i = Number(ini.value)
        let f = Number(fim.value)
        let p = Number(pas.value)
        for (var c = i; c <= f; Math.abs(p)){
            res.innerHTML += ` ${c} `
        }
    }
}