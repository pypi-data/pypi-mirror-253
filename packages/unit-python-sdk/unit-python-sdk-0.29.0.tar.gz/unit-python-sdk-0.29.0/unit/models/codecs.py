from unit.models.applicationForm import ApplicationFormDTO
from unit.models.application import IndividualApplicationDTO, BusinessApplicationDTO, ApplicationDocumentDTO,\
    TrustApplicationDTO
from unit.models.account import DepositAccountDTO, AccountDepositProductDTO, CreditAccountDTO, \
    CreditAccountLimitsDTO, DepositAccountLimitsDTO
from unit.models.check_payment import CheckPaymentDTO
from unit.models.customer import IndividualCustomerDTO, BusinessCustomerDTO
from unit.models.card import IndividualDebitCardDTO, BusinessDebitCardDTO, IndividualVirtualDebitCardDTO, \
    BusinessVirtualDebitCardDTO, PinStatusDTO, CardLimitsDTO, BusinessCreditCardDTO, BusinessVirtualCreditCardDTO, \
    MobileWalletPayloadDTO, CardToCardPaymentDTO
from unit.models.received_payment import AchReceivedPaymentDTO
from unit.models.repayment import BookRepaymentDTO, AchRepaymentDTO
from unit.models.transaction import transactions_mapper
from unit.models.payment import AchPaymentDTO, BookPaymentDTO, WirePaymentDTO, BillPaymentDTO, AchReceivedPaymentDTO, \
    RecurringCreditAchPaymentDTO, RecurringCreditBookPaymentDTO, RecurringDebitAchPaymentDTO, BulkPaymentsDTO
from unit.models.customerToken import CustomerTokenDTO, CustomerVerificationTokenDTO
from unit.models.fee import FeeDTO
from unit.models.event import *
from unit.models.counterparty import CounterpartyDTO, CounterpartyBalanceDTO
from unit.models.webhook import WebhookDTO
from unit.models.institution import InstitutionDTO
from unit.models.statement import StatementDTO
from unit.models.atm_location import AtmLocationDTO
from unit.models.bill_pay import BillerDTO
from unit.models.api_token import APITokenDTO
from unit.models.authorization import AuthorizationDTO
from unit.models.authorization_request import PurchaseAuthorizationRequestDTO, CardTransactionAuthorizationRequestDTO, \
    AtmAuthorizationRequestDTO
from unit.models.account_end_of_day import AccountEndOfDayDTO
from unit.models.check_deposit import CheckDepositDTO
from unit.models.dispute import DisputeDTO

mappings = {
        "individualApplication": lambda _id, _type, attributes, relationships:
        IndividualApplicationDTO.from_json_api(_id, _type, attributes, relationships),

        "businessApplication": lambda _id, _type, attributes, relationships:
        BusinessApplicationDTO.from_json_api(_id, _type, attributes, relationships),

        "trustApplication": lambda _id, _type, attributes, relationships:
        TrustApplicationDTO.from_json_api(_id, _type, attributes, relationships),

        "document": lambda _id, _type, attributes, relationships:
        ApplicationDocumentDTO.from_json_api(_id, _type, attributes),

        "individualCustomer": lambda _id, _type, attributes, relationships:
        IndividualCustomerDTO.from_json_api(_id, _type, attributes, relationships),

        "businessCustomer": lambda _id, _type, attributes, relationships:
        BusinessCustomerDTO.from_json_api(_id, _type, attributes, relationships),

        "depositAccount": lambda _id, _type, attributes, relationships:
        DepositAccountDTO.from_json_api(_id, _type, attributes, relationships),

        "creditAccount": lambda _id, _type, attributes, relationships:
        CreditAccountDTO.from_json_api(_id, _type, attributes, relationships),

        "limits": lambda _id, _type, attributes, relationships:
        decode_limits(_id, _type, attributes),

        "creditLimits": lambda _id, _type, attributes, relationships:
        CreditAccountLimitsDTO.from_json_api(_id, _type, attributes),

        "individualDebitCard": lambda _id, _type, attributes, relationships:
        IndividualDebitCardDTO.from_json_api(_id, _type, attributes, relationships),

        "businessDebitCard": lambda _id, _type, attributes, relationships:
        BusinessDebitCardDTO.from_json_api(_id, _type, attributes, relationships),

        "businessCreditCard": lambda _id, _type, attributes, relationships:
        BusinessCreditCardDTO.from_json_api(_id, _type, attributes, relationships),

        "individualVirtualDebitCard": lambda _id, _type, attributes, relationships:
        IndividualVirtualDebitCardDTO.from_json_api(_id, _type, attributes, relationships),

        "businessVirtualDebitCard": lambda _id, _type, attributes, relationships:
        BusinessVirtualDebitCardDTO.from_json_api(_id, _type, attributes, relationships),

        "businessVirtualCreditCard": lambda _id, _type, attributes, relationships:
        BusinessVirtualCreditCardDTO.from_json_api(_id, _type, attributes, relationships),

        "achPayment": lambda _id, _type, attributes, relationships:
        AchPaymentDTO.from_json_api(_id, _type, attributes, relationships),

        "bookPayment": lambda _id, _type, attributes, relationships:
        BookPaymentDTO.from_json_api(_id, _type, attributes, relationships),

        "wirePayment": lambda _id, _type, attributes, relationships:
        WirePaymentDTO.from_json_api(_id, _type, attributes, relationships),

        "billPayment": lambda _id, _type, attributes, relationships:
        BillPaymentDTO.from_json_api(_id, _type, attributes, relationships),

        "achReceivedPayment": lambda _id, _type, attributes, relationships:
        AchReceivedPaymentDTO.from_json_api(_id, _type, attributes, relationships),

        "recurringCreditAchPayment": lambda _id, _type, attributes, relationships:
        RecurringCreditAchPaymentDTO.from_json_api(_id, _type, attributes, relationships),

        "recurringCreditBookPayment": lambda _id, _type, attributes, relationships:
        RecurringCreditBookPaymentDTO.from_json_api(_id, _type, attributes, relationships),

        "recurringDebitAchPayment": lambda _id, _type, attributes, relationships:
        RecurringDebitAchPaymentDTO.from_json_api(_id, _type, attributes, relationships),

        "bulkPayments": lambda _id, _type, attributes, relationships:
        BulkPaymentsDTO.from_json_api(_type, attributes),

        "accountStatementDTO": lambda _id, _type, attributes, relationships:
        StatementDTO.from_json_api(_id, _type, attributes, relationships),

        "sandboxAccountStatement": lambda _id, _type, attributes, relationships:
        StatementDTO.from_json_api(_id, _type, attributes, relationships),

        "customerBearerToken": lambda _id, _type, attributes, relationships:
        CustomerTokenDTO.from_json_api(_id, _type, attributes, relationships),

        "customerTokenVerification": lambda _id, _type, attributes, relationships:
        CustomerVerificationTokenDTO.from_json_api(_id, _type, attributes, relationships),

        "achCounterparty": lambda _id, _type, attributes, relationships:
        CounterpartyDTO.from_json_api(_id, _type, attributes, relationships),

        "applicationForm": lambda _id, _type, attributes, relationships:
        ApplicationFormDTO.from_json_api(_id, _type, attributes, relationships),

        "fee": lambda _id, _type, attributes, relationships:
        FeeDTO.from_json_api(_id, _type, attributes, relationships),

        "account.closed": lambda _id, _type, attributes, relationships:
        AccountClosedEvent.from_json_api(_id, _type, attributes, relationships),

        "account.frozen": lambda _id, _type, attributes, relationships:
        AccountFrozenEvent.from_json_api(_id, _type, attributes, relationships),

        "application.awaitingDocuments": lambda _id, _type, attributes, relationships:
        ApplicationAwaitingDocumentsEvent.from_json_api(_id, _type, attributes, relationships),

        "application.denied": lambda _id, _type, attributes, relationships:
        ApplicationDeniedEvent.from_json_api(_id, _type, attributes, relationships),

        "application.pendingReview": lambda _id, _type, attributes, relationships:
        ApplicationPendingReviewEvent.from_json_api(_id, _type, attributes, relationships),

        "card.activated": lambda _id, _type, attributes, relationships:
        CardActivatedEvent.from_json_api(_id, _type, attributes, relationships),

        "card.statusChanged": lambda _id, _type, attributes, relationships:
        CardStatusChangedEvent.from_json_api(_id, _type, attributes, relationships),

        "authorization.created": lambda _id, _type, attributes, relationships:
        AuthorizationCreatedEvent.from_json_api(_id, _type, attributes, relationships),

        "authorizationRequest.declined": lambda _id, _type, attributes, relationships:
        AuthorizationRequestDeclinedEvent.from_json_api(_id, _type, attributes, relationships),

        "authorizationRequest.pending": lambda _id, _type, attributes, relationships:
        AuthorizationRequestPendingEvent.from_json_api(_id, _type, attributes, relationships),

        "authorizationRequest.approved": lambda _id, _type, attributes, relationships:
        AuthorizationRequestApprovedEvent.from_json_api(_id, _type, attributes, relationships),

        "document.approved": lambda _id, _type, attributes, relationships:
        DocumentApprovedEvent.from_json_api(_id, _type, attributes, relationships),

        "document.rejected": lambda _id, _type, attributes, relationships:
        DocumentRejectedEvent.from_json_api(_id, _type, attributes, relationships),

        "document.approved": lambda _id, _type, attributes, relationships:
        DocumentApprovedEvent.from_json_api(_id, _type, attributes, relationships),

        "checkDeposit.created": lambda _id, _type, attributes, relationships:
        CheckDepositCreatedEvent.from_json_api(_id, _type, attributes, relationships),

        "checkDeposit.clearing": lambda _id, _type, attributes, relationships:
        CheckDepositClearingEvent.from_json_api(_id, _type, attributes, relationships),

        "checkDeposit.sent": lambda _id, _type, attributes, relationships:
        CheckDepositSentEvent.from_json_api(_id, _type, attributes, relationships),

        "payment.clearing": lambda _id, _type, attributes, relationships:
        PaymentClearingEvent.from_json_api(_id, _type, attributes, relationships),

        "payment.sent": lambda _id, _type, attributes, relationships:
        PaymentSentEvent.from_json_api(_id, _type, attributes, relationships),

        "payment.returned": lambda _id, _type, attributes, relationships:
        PaymentReturnedEvent.from_json_api(_id, _type, attributes, relationships),

        "statements.created": lambda _id, _type, attributes, relationships:
        StatementsCreatedEvent.from_json_api(_id, _type, attributes, relationships),

        "transaction.created": lambda _id, _type, attributes, relationships:
        TransactionCreatedEvent.from_json_api(_id, _type, attributes, relationships),

        "customer.created": lambda _id, _type, attributes, relationships:
        CustomerCreatedEvent.from_json_api(_id, _type, attributes, relationships),

        "account.reopened": lambda _id, _type, attributes, relationships:
        AccountReopenedEvent.from_json_api(_id, _type, attributes, relationships),

        "webhook": lambda _id, _type, attributes, relationships:
        WebhookDTO.from_json_api(_id, _type, attributes, relationships),

        "institution": lambda _id, _type, attributes, relationships:
        InstitutionDTO.from_json_api(_id, _type, attributes, relationships),

        "atmLocation": lambda _id, _type, attributes, relationships:
        AtmLocationDTO.from_json_api(_type, attributes),

        "biller": lambda _id, _type, attributes, relationships:
        BillerDTO.from_json_api(_id, _type, attributes, relationships),

        "apiToken": lambda _id, _type, attributes, relationships:
        APITokenDTO.from_json_api(_id, _type, attributes, relationships),

        "authorization": lambda _id, _type, attributes, relationships:
        AuthorizationDTO.from_json_api(_id, _type, attributes, relationships),

        "purchaseAuthorizationRequest": lambda _id, _type, attributes, relationships:
        PurchaseAuthorizationRequestDTO.from_json_api(_id, _type, attributes, relationships),

        "cardTransactionAuthorizationRequest": lambda _id, _type, attributes, relationships:
        CardTransactionAuthorizationRequestDTO.from_json_api(_id, _type, attributes, relationships),

        "atmAuthorizationRequest": lambda _id, _type, attributes, relationships:
        AtmAuthorizationRequestDTO.from_json_api(_id, _type, attributes, relationships),

        "accountEndOfDay": lambda _id, _type, attributes, relationships:
        AccountEndOfDayDTO.from_json_api(_id, _type, attributes, relationships),

        "counterpartyBalance": lambda _id, _type, attributes, relationships:
        CounterpartyBalanceDTO.from_json_api(_id, _type, attributes, relationships),

        "pinStatus": lambda _id, _type, attributes, relationships:
        PinStatusDTO.from_json_api(attributes),

        "accountDepositProduct": lambda _id, _type, attributes, relationships:
        AccountDepositProductDTO.from_json_api(attributes),

        "checkDeposit": lambda _id, _type, attributes, relationships:
        CheckDepositDTO.from_json_api(_id, _type, attributes, relationships),

        "dispute": lambda _id, _type, attributes, relationships:
        DisputeDTO.from_json_api(_id, _type, attributes, relationships),

        "mobileWalletPayload": lambda _id, _type, attributes, relationships:
        MobileWalletPayloadDTO.from_json_api(_id, _type, attributes, relationships),

        "bookRepayment": lambda _id, _type, attributes, relationships:
        BookRepaymentDTO.from_json_api(_id, _type, attributes, relationships),

        "achRepayment": lambda _id, _type, attributes, relationships:
        AchRepaymentDTO.from_json_api(_id, _type, attributes, relationships),

        "astra": lambda _id, _type, attributes, relationships:
        CardToCardPaymentDTO.from_json_api(_id, _type, attributes, relationships),

        "beneficialOwner": lambda _id, _type, attributes, relationships:
        BeneficialOwnerDTO.from_json_api(_id, _type, attributes, relationships),

        "checkPayment": lambda _id, _type, attributes, relationships:
        CheckPaymentDTO.from_json_api(_id, _type, attributes, relationships)
    }


def split_json_api_single_response(payload: Dict):
    _id, _type, attributes = payload.get("id"), payload["type"], payload["attributes"]
    relationships = None

    if payload.get("relationships"):
        relationships = dict()
        for k, v in payload.get("relationships").items():
            if isinstance(v["data"], list):
                relationships[k] = RelationshipArray(v["data"])
            else:
                relationships[k] = Relationship(v["data"]["type"], v["data"]["id"])

    return _id, _type, attributes, relationships


def split_json_api_array_response(payload):
    if not isinstance(payload, list):
        raise Exception("split_json_api_array_response - couldn't parse response.")

    dtos = []
    for single_obj in payload:
        dtos.append(split_json_api_single_response(single_obj))

    return dtos


def decode_limits(_id: str, _type: str, attributes: Dict):
    if "ach" in attributes.keys():
        return DepositAccountLimitsDTO.from_json_api(_id, _type, attributes)
    else:
        return CardLimitsDTO.from_json_api(attributes)


def mapping_wrapper(_id, _type, attributes, relationships):
    if _type in mappings:
        return mappings[_type](_id, _type, attributes, relationships)
    if "Transaction" in _type:
        return transactions_mapper(_id, _type, attributes, relationships)
    else:
        return RawUnitObject(_id, _type, attributes, relationships)


class DtoDecoder(object):
    @staticmethod
    def decode(payload):
        if payload is None:
            return None
        # if response contains a list of dtos
        if isinstance(payload, list):
            dtos = split_json_api_array_response(payload)
            response = []
            for _id, _type, attributes, relationships in dtos:
                response.append(mapping_wrapper(_id, _type, attributes, relationships))

            return response
        else:
            _id, _type, attributes, relationships = split_json_api_single_response(payload)
            return mapping_wrapper(_id, _type, attributes, relationships)


class UnitEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        if hasattr(obj, 'to_dict'):
            return obj.to_dict()
        else:
            try:
                return json.JSONEncoder.default(self, obj)
            except TypeError:
                return json.dumps(obj, default=lambda o: o.__dict__, sort_keys=True, indent=4)

