from django.test import TestCase

payload = {
    "configuration": {
        "stickerSendingDisabled": True,
        "cannotStartConversation": False,
        "multipleRecipientsDisabled": True
    },

    "supervisedTeams":[
        {
            "id": f"{codigo_vendedor}",
            "name": f"{descricao_vendas}"
        }
    ],
    "supervisedTeams":[
        {
            "id": f"{codigo_gestao}",
            "name": f"{descricao_gestao}"
        }
    ],

    "teams":[
        {
            "id": f"{codigo_gestao}",
            "name": f"{descricao_gestao}"
        }
    ],

    "name": f"{nome}",
    "username": f"{email}",
    "password": f"{senha}",
    "salesPersonCode": f"{matricula}",
    "roles": ["service", "supervisor"]
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "x-api-key": "PQRBLpZj2U7P97QrIQrTu7uukbVhkVZu2S0mppWd",
    "x-api-secret": "r:7a2fb21821337f4c8d3f15a471030b2e"
}
