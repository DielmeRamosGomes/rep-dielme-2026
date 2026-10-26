class Pessoa {
    constructor(nome, idade) {
        this.__nome = nome;
        this.__idade = idade;
    }

    getNome() {
        return this.__nome;
    }

    getIdade() {
        return this.__idade;
    }

    setNome(novoNome) {
        this.__nome = novoNome;
    }

    setIdade(novaIdade) {
        this.__idade = novaIdade;
    }
} export default Pessoa;







