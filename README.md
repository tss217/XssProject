# XSS Tools

## Descrição
Este repositório contém ferramentas para a detecção e prevenção de ataques de Cross-Site Scripting (XSS). As ferramentas foram desenvolvidas para ajudar desenvolvedores e administradores de sistemas a protegerem suas aplicações web contra vulnerabilidades de XSS.

## Funcionalidades
- Detecção de vulnerabilidades XSS em aplicações web.
- Ferramentas para sanitização de entradas de usuário.
- Relatórios detalhados sobre possíveis pontos de ataque.

## Como Usar
1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/xss-tools.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd xss-tools
    ```
3. Siga as instruções específicas de cada ferramenta no diretório `tools`.

## Contribuição
Contribuições são bem-vindas! Por favor, siga as etapas abaixo para contribuir:
1. Faça um fork do repositório.
2. Crie uma nova branch com sua feature ou correção de bug:
    ```bash
    git checkout -b minha-feature
    ```
3. Faça commit das suas alterações:
    ```bash
    git commit -m 'Adiciona minha feature'
    ```
4. Envie para o branch original:
    ```bash
    git push origin minha-feature
    ```
5. Abra um Pull Request.

### Argumentos
- `--url`: URL alvo para testar (obrigatório).
- `-w`: Caminho para o arquivo de wordlist (obrigatório).
- `-oB`: Abre o navegador se um payload XSS for encontrado (opcional).
- `-t`: Tempo de espera entre cada teste em segundos (opcional, padrão é 0).
- `-aOB`: Sempre abre o navegador após cada teste, independentemente do resultado (opcional).

### Exemplo de Uso
python3 main.py --url https://www.google.com/search?q= -w path/to/wordlist.txt -oB -t 5 -aOB


## Responsabilidade
O usuário é responsável por garantir que as ferramentas sejam usadas de maneira ética e legal. O uso inadequado das ferramentas pode resultar em consequências legais. Este repositório é fornecido "como está", sem garantias de qualquer tipo.

## Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
