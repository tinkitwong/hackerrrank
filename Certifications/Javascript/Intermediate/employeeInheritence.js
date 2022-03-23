function Employee (title) {
    this.title = title;
}

Employee.prototype.setTitle = function (title) {
    this.title = title;
}

Employee.prototype.getTitle = function () {
    return this.title;
}

function Engineer (title, isManager) {
    Employee.call(this, title);
    this.isManager = isManager;
}

Object.setPrototypeOf(Employee.prototype, Engineer.prototype);

/** Getter Setter Methods */
Engineer.prototype.getisManager = function () {
    return this.isManager;
}

Engineer.prototype.setIsManager = function (isManager) {
    this.isManager = isManager;
}