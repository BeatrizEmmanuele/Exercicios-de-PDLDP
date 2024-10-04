public class ex12 {
    // Classe Produto
    private String nome;
    private double preco;

    public ex12(String nome, double preco) {
        this.nome = nome;
        this.preco = preco;
    }

    public ex12 somar(ex12 outro) {
        return new ex12(this.nome + " & " + outro.nome, this.preco + outro.preco);
    }

    @Override
    public String toString() {
        return "Produto: " + nome + ", Preço: R$" + String.format("%.2f", preco);
    }

    public static void main(String[] args) {
        ex12 produto1 = new ex12("Produto A", 50.0);
        ex12 produto2 = new ex12("Produto B", 30.0);

        ex12 produtoCombinado = produto1.somar(produto2);
        System.out.println(produtoCombinado); // Produto: Produto A & Produto B, Preço: R$80.00
    }
}
