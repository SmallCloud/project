# coding: utf-8
# © 2015 David BEAL @ Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, api, _


# generated by print ''.join([str(ord(x)) for x in 'model_to_project_task'])
UNIQUE_ACTION_ID = (
    1091111001011089511611195112114111106101991169511697115107)


class IrValues(models.Model):
    _inherit = 'ir.values'

    @api.model
    def get_actions(self, action_slot, model, res_id=False):
        """ Add an action to all Model objects of the ERP """
        res = super(IrValues, self).get_actions(
            action_slot, model, res_id=res_id)
        available_models = [
            x[0] for x in self.env['project.task']._authorised_models()
            if x[0] != 'project.task']
        if action_slot == 'client_action_multi' and model in available_models:
            action = self.set_task_action(model, res_id=res_id)
            value = (UNIQUE_ACTION_ID, 'model_to_project_task', action)
            res.insert(0, value)
        return res

    @api.model
    def set_task_action(self, model, res_id=False):
        action_id = self.env.ref(
            'model_to_project_task.task_from_elsewhere').id
        return {
            'id': action_id,
            'name': _('Define a task'),
            'res_model': u'project.task',
            'src_model': model,
            'type': u'ir.actions.act_window',
            'target': 'current',
        }
