class Table:
    def __init__(self, customers: int):
        self.customers = customers
        self.bill = list()

    def order(self, item, price, quantity=1.0):
        current_order = {"item": item, "price": price, "quantity": quantity}
        counter = 0

        for instance in self.bill:  # first check if in the bill
            if instance["item"] == current_order["item"] and instance["price"] == current_order["price"]:
                current_order["quantity"] += instance["quantity"]
                self.bill[counter] = current_order
                return
            counter += 1

        self.bill.append(current_order)
        return

    def remove(self, item, price, quantity=1.0):
        temp_order = {"item": item, "price": price, "quantity": quantity}
        counter = 0

        for instance in self.bill:
            if instance["item"] == temp_order["item"] and instance["price"] == temp_order["price"]:
                if instance["quantity"] > temp_order["quantity"]:
                    # if instance from main list has more quantities than we need to remove
                    temp_order["quantity"] = instance["quantity"] - quantity  # update quantity
                    self.bill[counter] = temp_order  # push
                    return
                else:  # if quantity is equal
                    self.bill.pop(counter)  # remove
                    return
        if len(self.bill) == 0:
            return
        counter += 1

    def get_subtotal(self):
        total = 0
        for instance in self.bill:
            for i in range(instance["quantity"]):
                total += instance["price"]
        return total

    def get_total(self, charge=0.1):
        price = self.get_subtotal()
        charge_pounds = price * charge
        return {"Sub Total": f"£{format(price, '.2f')}", "Service Charge": f"£{format(charge_pounds, '.2f')}",
                "Total": f"£{format(price + charge_pounds, '.2f')}"}

    def split_bill(self):
        final_price = self.get_subtotal()
        return final_price / self.customers


# t = Table(1)
# t.order("1", 1.0)
# t.order("1", 1.0)
# t.order("1", 1.0)
# t.order("2", 1.0)
# t.order("2", 1.0)
# t.order("2", 1.0)
# t.order("1", 2.0)
# t.order("2", 4.0)
# t.remove("1", 1.0, 3)
# print(t.bill[0]["quantity"])
