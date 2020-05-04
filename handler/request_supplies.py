from flask import jsonify
from dao.request_supplies import RequestedSuppliesDAO


class RequestedSuppliesHandler:
    def build_request_supplies_dict(self, row):
        result = {}
        result['aid'] = row[0]
        result['sid'] = row[1]
        result['request_type'] = row[2]
        result['request_quantity'] = row[3]
        result['request_brand'] = row[4]
        return result

    # def build_consumer_attributes(self, cid, cfirstname, clastname, clocation, cage, cphone):
    #     result = {}
    #     result['cid'] = cid
    #     result['cfirstname'] = cfirstname
    #     result['clastname'] = clastname
    #     result['clocation'] = clocation
    #     result['cage'] = cage
    #     result['cphone'] = cphone
    #     return result

    def getAllRequestedSupplies(self):
        dao = RequestedSuppliesDAO()
        request_supplies_list = dao.getAllRequestedSupplies()
        result_list = []
        for row in request_supplies_list:
            result = self.build_request_supplies_dict(row)
            result_list.append(result)
        return jsonify(RequestedSupplies=result_list)

    def searchRequestedSupplies(self, args):
        type = args.get("type")
        dao = RequestedSuppliesDAO()
        requested_supplies_list = []
        if (len(args) == 1) and type:
            requested_supplies_list = dao.getRequestedSuppliesByType(type)
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in requested_supplies_list:
            result = self.build_request_supplies_dict(row)
            result_list.append(result)
        return jsonify(RequestedSupplies=result_list)

    # def getConsumerById(self, cid):
    #     dao = ConsumersDAO()
    #     row = dao.getConsumerById(cid)
    #     if not row:
    #         return jsonify(Error="Part Not Found"), 404
    #     else:
    #         consumer = self.build_consumer_dict(row)
    #         return jsonify(Consumer=consumer)
    #
    # def searchConsumers(self, args):
    #     name = args.get("name")
    #     dao = ConsumersDAO()
    #     consumers_list = []
    #     if (len(args) == 1) and name:
    #         consumers_list = dao.getConsumerByName(name)
    #     else:
    #         return jsonify(Error = "Malformed query string"), 400
    #     result_list = []
    #     for row in consumers_list:
    #         result = self.build_consumer_dict(row)
    #         result_list.append(result)
    #     return jsonify(Consumers=result_list)
    #
    #
    # def insertConsumer(self, form):
    #     print("form: ", form)
    #     if len(form) != 4:
    #         return jsonify(Error = "Malformed post request"), 400
    #     else:
    #         cfirstname = form['cfirstname']
    #         clastname = form['clastname']
    #         clocation = form['clocation']
    #         cage = form['cage']
    #         cphone = form['cphone']
    #
    #         if cfirstname and clastname and clocation and cage and cphone:
    #             dao = ConsumersDAO()
    #             cid = dao.insert(cfirstname, clastname, clocation, cage, cphone)
    #             result = self.build_consumer_attributes(cid, cfirstname, clastname, clocation, cage, cphone)
    #             return jsonify(Part=result), 201
    #         else:
    #             return jsonify(Error="Unexpected attributes in post request"), 400
    #
    # def insertConsumerJson(self, json):
    #     cfirstname = json['cfirstname']
    #     clastname = json['clastname']
    #     clocation = json['clocation']
    #     cage = json['cage']
    #     cphone = json['cphone']
    #     if cfirstname and clastname and clocation and cage and cphone:
    #         dao = ConsumersDAO()
    #         result = dao.insert(cfirstname, clastname, clocation, cage, cphone)
    #         return jsonify(Consumer=result), 201
    #     else:
    #         return jsonify(Error="Unexpected attributes in post request"), 400
    #
    # def deleteConsumer(self, cid):
    #     dao = ConsumersDAO()
    #     # if not dao.getConsumerById(cid):
    #     #     return jsonify(Error = "Part not found."), 404
    #     # else:
    #     result = dao.delete(cid)
    #     return jsonify(DeleteStatus = result), 200
    #
    # def updateConsumer(self, cid, form):
    #     dao = ConsumersDAO()
    #     if not dao.getConsumerById(cid):
    #         return jsonify(Error = "Consumer not found."), 404
    #     else:
    #         return jsonify(dao.getConsumerById(cid)), 201





