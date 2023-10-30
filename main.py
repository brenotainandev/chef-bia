import json
import speech_recognition as sr
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Carregar as configurações do arquivo JSON
with open("config.json", "r") as config_file:
    configuracao = json.load(config_file)

IDIOMA_FALA = "pt-BR"
IDIOMA_CORPUS = "portuguese"
NOME_ASSISTENTE = configuracao["nome"]

# Carregar as palavras de parada em português
stop_words = set(stopwords.words(IDIOMA_CORPUS))


def iniciar():
    global reconhecedor
    reconhecedor = sr.Recognizer()


def escutar_comando():
    global reconhecedor
    comando = None
    with sr.Microphone() as fonte_audio:
        reconhecedor.adjust_for_ambient_noise(fonte_audio)
        print("Fale o seu comando:")
        try:
            fala = reconhecedor.listen(
                fonte_audio, timeout=5, phrase_time_limit=5
            )
            comando = reconhecedor.recognize_google(fala, language=IDIOMA_FALA)
            if not comando.lower().startswith(NOME_ASSISTENTE.lower()):
                print("Comando não reconhecido. Repita, por favor!")
                return ""
        except sr.UnknownValueError:
            print("Tempo limite atingido. Tente novamente.")
    return comando


def processar_audio_do_comando(audio_do_comando):
    global reconhecedor

    comando = None

    with sr.AudioFile(audio_do_comando) as fonte_audio:
        fala = reconhecedor.listen(fonte_audio)
        try:
            comando = reconhecedor.recognize_google(fala, language=IDIOMA_FALA)
        except sr.UnknownValueError:
            print("Falha ao processar audio do comando.")

    return comando


def processar_comando(comando):
    global configuracao
    if not isinstance(comando, str):
        print("Comando inválido. Repita, por favor!")
        return None

    # Tokenize e remova palavras de parada
    tokens = word_tokenize(comando, language=IDIOMA_CORPUS)
    tokens = [word for word in tokens if word not in stop_words]

    acao_correspondente = None

    for acao, palavras_chave in configuracao["acoes"].items():
        if any(palavra_chave in comando for palavra_chave in palavras_chave):
            acao_correspondente = acao
            break

    if acao_correspondente == "encerrar":
        return "encerrar"

    return acao_correspondente


def executar_acao(acao):
    if acao:
        if acao == "encerrar":
            print("Encerrando a aplicação. Um beijo da Bia, até breve!!")
            global continuar
            continuar = False
        else:
            print(f"Executando a ação: {acao}")
    else:
        print("Comando não reconhecido. Repita, por favor!")


def main():
    iniciar()
    continuar = True
    while continuar:
        try:
            comando = escutar_comando()
            print(f"Processando o comando: {comando}")
            acao = processar_comando(comando)
            if acao == "encerrar":
                print("Encerrando a aplicação. Um beijo da Bia, até breve!!")
                continuar = False
            else:
                executar_acao(acao)
        except KeyboardInterrupt:
            print("Um beijo da Bia, até breve!")
            continuar = False


if __name__ == "__main__":
    main()
