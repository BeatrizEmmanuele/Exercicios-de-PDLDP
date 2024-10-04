public class ex14 {
    // Atributo estático para armazenar a instância única
    private static ex14 instancia;

    // Atributos de configuração (exemplo)
    private String nomeBanco;
    private String urlBanco;

    // Construtor privado para evitar a instância externa
    private ex14() {
        // Inicializações de configuração
        nomeBanco = "MeuBanco";
        urlBanco = "jdbc:meubanco://localhost:3306/minha_base";
    }

    // Método estático para obter a instância única
    public static ex14 getInstancia() {
        if (instancia == null) {
            instancia = new ex14();
        }
        return instancia;
    }

    // Métodos de configuração (getters)
    public String getNomeBanco() {
        return nomeBanco;
    }

    public String getUrlBanco() {
        return urlBanco;
    }

    // Método para testar a classe Singleton
    public static void main(String[] args) {
        ex14 config1 = ex14.getInstancia();
        ex14 config2 = ex14.getInstancia();

        // Verificando se ambas referências apontam para a mesma instância
        System.out.println("Configuração 1: " + config1.getNomeBanco());
        System.out.println("Configuração 2: " + config2.getNomeBanco());
        System.out.println("As instâncias são iguais? " + (config1 == config2)); // true
    }
}
