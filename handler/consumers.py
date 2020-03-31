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
        result_list = dao.getAllConsumers()
        return jsonify(Consumers=result_list)

    def getConsumerById(self, cid):
        dao = ConsumersDAO()
        result = dao.getConsumerById(cid)
        return jsonify(Consumers=result)

    def searchConsumers(self, args):
        name = args.get("name")
        dao = ConsumersDAO()
        results_list = []
        if (len(args) == 1) and name:
            results_list = dao.getConsumerByName(name)
        else:
            results_list = dao.searchConsumerBeta()
        return jsonify(Consumers=results_list)


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
        if not dao.getConsumerById(cid):
            return jsonify(Error = "Part not found."), 404
        else:
            dao.delete(cid)
            return jsonify(DeleteStatus = "OK"), 200

    def updateConsumer(self, cid, form):
        dao = ConsumersDAO()
        if not dao.getConsumerById(cid):
            return jsonify(Error = "Consumer not found."), 404
        else:
            return jsonify(dao.getConsumerById(cid)), 201




