from flask import jsonify
from dao.consumer import ConsumersDAO


class ConsumerHandler:
    def build_consumer_dict(self, row):
        result = {}
        result['cid'] = row[0]
        result['cfirstname'] = row[1]
        result['clastname'] = row[2]
        result['clocation'] = row[3]
        result['cage'] = row[4]
        result['cphone'] = row[5]
        return result

    def build_consumer_attributes(self, cid, cfirstname, clastname, clocation, cage, cphone):
        result = {}
        result['cid'] = cid
        result['cfirstname'] = cfirstname
        result['clastname'] = clastname
        result['clocation'] = clocation
        result['cage'] = cage
        result['cphone'] = cphone
        return result

    def getAllConsumers(self):
        dao = ConsumersDAO()
        consumers_list = dao.getAllConsumers()
        result_list = []
        for row in consumers_list:
            result = self.build_consumer_dict(row)
            result_list.append(result)
        return jsonify(Consumers=result_list)

    def getConsumerById(self, cid):
        dao = ConsumersDAO()
        row = dao.getConsumerById(cid)
        if not row:
            return jsonify(Error="Part Not Found"), 404
        else:
            consumer = self.build_consumer_dict(row)
            return jsonify(Consumer=consumer)

    def searchConsumers(self, args):
        name = args.get("name")
        dao = ConsumersDAO()
        consumers_list = []
        if (len(args) == 1) and name:
            consumers_list = dao.getConsumerByName(name)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in consumers_list:
            result = self.build_consumer_dict(row)
            result_list.append(result)
        return jsonify(Consumers=result_list)


    def insertConsumer(self, form):
        print("form: ", form)
        if len(form) != 4:
            return jsonify(Error = "Malformed post request"), 400
        else:
            cfirstname = form['cfirstname']
            clastname = form['clastname']
            clocation = form['clocation']
            cage = form['cage']
            cphone = form['cphone']

            if cfirstname and clastname and clocation and cage and cphone:
                dao = ConsumersDAO()
                cid = dao.insert(cfirstname, clastname, clocation, cage, cphone)
                result = self.build_consumer_attributes(cid, cfirstname, clastname, clocation, cage, cphone)
                return jsonify(Part=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def insertConsumerJson(self, json):
        cfirstname = json['cfirstname']
        clastname = json['clastname']
        clocation = json['clocation']
        cage = json['cage']
        cphone = json['cphone']
        if cfirstname and clastname and clocation and cage and cphone:
            dao = ConsumersDAO()
            result = dao.insert(cfirstname, clastname, clocation, cage, cphone)
            return jsonify(Consumer=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteConsumer(self, cid):
        dao = ConsumersDAO()
        # if not dao.getConsumerById(cid):
        #     return jsonify(Error = "Part not found."), 404
        # else:
        result = dao.delete(cid)
        return jsonify(DeleteStatus = result), 200

    def updateConsumer(self, cid, form):
        dao = ConsumersDAO()
        if not dao.getConsumerById(cid):
            return jsonify(Error = "Consumer not found."), 404
        else:
            return jsonify(dao.getConsumerById(cid)), 201




