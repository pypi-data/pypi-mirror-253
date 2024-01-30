from bamt_light.networks.discrete_bn import DiscreteBN
from bamt_light.utils import serialization_utils
import bamt_light.preprocessors as pp
from sklearn import preprocessing


class WorkDefectNet(DiscreteBN):
    def __init__(self, structure):
        super(WorkDefectNet, self).__init__()
        self.structure = structure

    def load(self, model_structure: dict, models_dir: str = "/"):
        self.add_nodes(model_structure["info"])
        self.set_structure(edges=model_structure["edges"])
        if not self.use_mixture:
            for node_data in model_structure["parameters"].values():
                if "hybcprob" not in node_data.keys():
                    continue
                else:
                    # Since we don't have information about types of nodes, we
                    # should derive it from parameters.
                    if any(
                        list(node_keys.keys()) == ["covars", "mean", "coef"]
                        for node_keys in node_data["hybcprob"].values()
                    ):
                        print(
                            f"This crucial parameter is not the same as father's parameter: use_mixture."
                        )
                        return

        # check if edges before and after are the same.They can be different in
        # the case when user sets forbidden edges.
        if not self.has_logit:
            if not all(
                edges_before == [edges_after[0], edges_after[1]]
                for edges_before, edges_after in zip(
                    model_structure["edges"], self.edges
                )
            ):
                print(
                    f"This crucial parameter is not the same as father's parameter: has_logit."
                )
                return

        deserializer = serialization_utils.Deserializer(models_dir)

        to_deserialize = {}
        # separate logit and gaussian nodes from distributions to deserialize bn's models
        for node_name in model_structure["parameters"].keys():
            if (
                "Gaussian" in self[node_name].type
                or "Logit" in self[node_name].type
                or "ConditionalLogit" in self[node_name].type
                or "ConditionalGaussian" in self[node_name].type
            ):
                if model_structure["parameters"][node_name].get("serialization", False):
                    to_deserialize[node_name] = [
                        self[node_name].type,
                        model_structure["parameters"][node_name],
                    ]
                elif "hybcprob" in model_structure["parameters"][node_name].keys():
                    to_deserialize[node_name] = [
                        self[node_name].type,
                        model_structure["parameters"][node_name],
                    ]
                else:
                    continue

        deserialized_parameters = deserializer.apply(to_deserialize)
        distributions = model_structure["parameters"].copy()

        for serialized_node in deserialized_parameters.keys():
            distributions[serialized_node] = deserialized_parameters[serialized_node]

        self.set_parameters(parameters=distributions)

        str_keys = list(model_structure["weights"].keys())
        tuple_keys = [eval(key) for key in str_keys]
        weights = {}
        for tuple_key in tuple_keys:
            weights[tuple_key] = model_structure["weights"][str(tuple_key)]
        self.weights = weights
        return True

    def fit(self, data):
        encoder = preprocessing.LabelEncoder()
        p = pp.Preprocessor([("encoder", encoder)])
        coded_data, _ = p.apply(data)
        self.add_nodes(p.info)
        self.set_structure(edges=self.structure)
        self.fit_parameters(data)

    def get_defect_probability(self, evidence):
        try:
            # sample = self.sample(1000, evidence=evidence)
            # prob_dict = (sample['class_child'].value_counts() / sample.shape[0]).to_dict()
            probs = self.get_dist("class_child", evidence)
            vals = self.distributions["class_child"]["vals"]
            prob_dict = dict()
            for i, v in enumerate(vals):
                prob_dict[v] = probs[i]
            top_n = dict(sorted(prob_dict.items(), key=itemgetter(1), reverse=True))
            return top_n
        except:
            return {}

    # def get_defect_res_probability(self, evidence):
    #     try:
    #         # sample = self.sample(1000, evidence=evidence)
    #         # prob_dict = (sample['res_child'].value_counts() / sample.shape[0]).to_dict()
    #         probs = self.get_dist('res_child', evidence)
    #         vals = self.distributions['res_child']['vals']
    #         prob_dict = dict()
    #         for i, v in enumerate(vals):
    #             prob_dict[v] = probs[i]
    #         top_n = dict(sorted(prob_dict.items(), key=itemgetter(1), reverse=True))
    #         return top_n
    #     except:
    #         return {}
    # def get_defect_res_hours(self, evidence, quantile=0.5):
    #     try:
    #         # sample = self.sample(1000, evidence=evidence)
    #         # quntile_value = np.quantile(sample['res_child_hours'].values,q=quantile)
    #         mu, var = self.get_dist('res_child_hours', evidence)
    #         if var == 0:
    #             return mu
    #         elif math.isnan(mu):
    #             return 0
    #         else:
    #             quantile_value = stats.norm.ppf(q=quantile, loc=mu, scale=var)
    #             return quantile_value
    #     except:
    #         return 0
    # def get_defect_res_users(self, evidence, quantile=0.5):
    #     try:
    #         # sample = self.sample(1000, evidence=evidence)
    #         # quntile_value = np.quantile(sample['res_child_users'].values,q=quantile)
    #         mu, var = self.get_dist('res_child_users', evidence)
    #         if var == 0:
    #             return mu
    #         elif math.isnan(mu):
    #             return 0
    #         else:
    #             quantile_value = stats.norm.ppf(q=quantile, loc=mu, scale=var)
    #             return quantile_value
    #     except:
    #         return 0
