import mercadopago

# Substitua pelo seu access token
ACCESS_TOKEN = "APP_USR-2605009467633910-060421-621fcebb74d9e7c602f16746c4b83883-1842227027"

# Inicializa o SDK do MercadoPago
sdk = mercadopago.SDK(ACCESS_TOKEN)

# Função para obter o pagamento por ID
def get_payment_by_id(payment_id):
    try:
        # Obtém o pagamento pela API
        payment_info = sdk.payment().get(payment_id)
        return payment_info
    except Exception as e:
        print(f"Erro ao obter pagamento: {e}")
        return None

# Substitua pelo ID do pagamento que deseja consultar