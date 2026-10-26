import Pessoa from "./Pessoa.js";

const pessoa = new Pessoa("João", 30);
console.log(pessoa.getNome());
console.log(pessoa.getIdade());

console.log("Alterando os valores...");
pessoa.setNome("Maria");
pessoa.setIdade(40);
console.log(pessoa.getNome());
console.log(pessoa.getIdade());
