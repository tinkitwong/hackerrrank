function Activity(amount) {
    this.amount = amount;
}

function Payment(amount, receiver) {
    Activity.call(this, amount);
    this.receiver = receiver;
}

function Refund(amount, sender) {
    Activity.call(this, amount);
    this.sender = sender;
}

Object.setPrototypeOf(Payment.prototype, Activity.prototype);
Object.setPrototypeOf(Refund.prototype, Activity.prototype);

Activity.prototype.setAmount = function (value) {
    if (value <= 0) {
        return false;
    } else {
        this.amount = value;
        return true;
    }
}

Activity.prototype.getAmount = function () {
    return this.amount;
}

Payment.prototype.setReceiver = function (receiver) {
    this.receiver = receiver;
}

Payment.prototype.getReceiver = function () {
    return this.receiver;
}

Refund.prototype.setSender = function (sender) {
    this.sender = sender;
}

Refund.prototype.getSender = function () {
    return this.sender;
}

const PaymentObj = new Payment(5000, "John")
console.log(PaymentObj)
console.log(PaymentObj.getAmount())