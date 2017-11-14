from flask import render_template, session, url_for, flash
from werkzeug.utils import redirect

from app.main.forms import EditForm, EditeCNSForm, EditeAPPForm, EditeNBForm, EditUEForm, EditPsUeForm
from app.models import Element, Type, Ecns, Eapp, Frequency, Enb, UE, UeModel, PsUe, Board
from . import main
from .. import db


@main.route('/', methods=['GET', 'POST'])
def index():
    # elements = Element.query.order_by(Element.type_id).all()
    simulation_elements = Element.query.filter(Element.usage == 'simulation').all()
    simulation_num = len(simulation_elements)
    real_elements = Element.query.filter(Element.usage == 'real').all()
    real_num = len(real_elements)
    return render_template('index.html', simu_num=simulation_num, real_num=real_num,
                           simulation_elements=simulation_elements,
                           real_elements=real_elements)


@main.route('/add-element', methods=['GET', 'POST'])
def add_element():
    form = EditForm()
    if form.validate_on_submit():
        element = Element(ip=form.ip.data, username=form.username.data,
                          password=form.password.data, type=Type.query.get(form.type.data),
                          usage=form.usage.data, pc_ip=form.pc_ip.data)
        db.session.add(element)
        db.session.commit()
        flash('Add element successfully')
        return redirect(url_for('.index'))
    return render_template('add_element.html', form=form)


@main.route('/edit-element/<int:id>', methods=['GET', 'POST'])
def edit_element(id):
    element = Element.query.get_or_404(id)
    form = EditForm()
    if form.validate_on_submit():
        element.ip = form.ip.data
        element.username = form.username.data
        element.password = form.password.data
        element.type = Type.query.get(form.type.data)
        element.usage = form.usage.data
        element.pc_ip = form.pc_ip.data
        db.session.add(element)
        db.session.commit()
        flash('The element has been updated')
        return redirect(url_for('.index'))
    form.ip.data = element.ip
    form.username.data = element.username
    form.password.data = element.password
    form.type.data = element.type_id
    form.usage.data = element.usage
    form.pc_ip.data = element.pc_ip
    return render_template('add_element.html', form=form)


@main.route('/delete-element/<int:id>', methods=['GET', 'POST'])
def delete_element(id):
    element = Element.query.get_or_404(id)
    db.session.delete(element)
    db.session.commit()
    return redirect(url_for('.index'))


@main.route('/add-ecns', methods=['GET', 'POST'])
def add_ecns():
    form = EditeCNSForm()
    if form.validate_on_submit():
        ecns = Ecns(ip=form.ip.data, username=form.username.data,
                    password=form.password.data,
                    usage=form.usage.data, pc_ip=form.pc_ip.data)
        db.session.add(ecns)
        db.session.commit()
        flash('Add eCNS210 successfully')
        return redirect(url_for('.ecns'))
    return render_template('add_ecns.html', form=form)


@main.route('/ecns', methods=['GET', 'POST'])
def ecns():
    # elements = Element.query.order_by(Element.type_id).all()
    simulation_ecns = Ecns.query.filter(Ecns.usage == 'simulation').all()
    simulation_num = len(simulation_ecns)
    real_ecns = Ecns.query.filter(Ecns.usage == 'real').all()
    real_num = len(real_ecns)
    return render_template('ecns.html', simu_num=simulation_num, real_num=real_num,
                           simulation_ecns=simulation_ecns,
                           real_ecns=real_ecns)


@main.route('/edit-ecns/<int:id>', methods=['GET', 'POST'])
def edit_ecns(id):
    ecns = Ecns.query.get_or_404(id)
    form = EditeCNSForm()
    if form.validate_on_submit():
        ecns.ip = form.ip.data
        ecns.username = form.username.data
        ecns.password = form.password.data
        ecns.usage = form.usage.data
        ecns.pc_ip = form.pc_ip.data
        db.session.add(ecns)
        db.session.commit()
        flash('The eCNS210 has been updated')
        return redirect(url_for('.ecns'))
    form.ip.data = ecns.ip
    form.username.data = ecns.username
    form.password.data = ecns.password
    form.usage.data = ecns.usage
    form.pc_ip.data = ecns.pc_ip
    return render_template('add_ecns.html', form=form)


@main.route('/delete-ecns/<int:id>', methods=['GET', 'POST'])
def delete_ecns(id):
    ecns = Ecns.query.get_or_404(id)
    db.session.delete(ecns)
    db.session.commit()
    return redirect(url_for('.ecns'))


@main.route('/eapp', methods=['GET', 'POST'])
def eapp():
    eapps = Eapp.query.order_by(Eapp.mdc_ip).all()
    # simulation_ecns = Ecns.query.filter(Ecns.usage == 'simulation').all()
    # simulation_num = len(simulation_ecns)
    # real_ecns = Ecns.query.filter(Ecns.usage == 'real').all()
    # real_num = len(real_ecns)
    return render_template('eapp.html', eapps=eapps)


@main.route('/add-eapp', methods=['GET', 'POST'])
def add_eapp():
    form = EditeAPPForm()
    if form.validate_on_submit():
        eapp = Eapp(mdc_ip=form.mdc_ip.data,
                    mdc_username=form.mdc_username.data,
                    mdc_password=form.mdc_password.data,
                    udc_ip=form.udc_ip.data,
                    udc_username=form.udc_username.data,
                    udc_password=form.udc_password.data,
                    # root_username=form.root_username.data,
                    root_password=form.root_password.data,
                    # ubp_username=form.ubp_username.data,
                    ubp_password=form.ubp_password.data
                    )
        db.session.add(eapp)
        db.session.commit()
        flash('Add eAPP successfully')
        return redirect(url_for('.eapp'))
    return render_template('add_eapp.html', form=form)


@main.route('/edit-eapp/<int:id>', methods=['GET', 'POST'])
def edit_eapp(id):
    eapp = Eapp.query.get_or_404(id)
    form = EditeAPPForm()
    if form.validate_on_submit():
        eapp.mdc_ip = form.mdc_ip.data
        eapp.mdc_username = form.mdc_username.data
        eapp.mdc_password = form.mdc_password.data
        eapp.udc_ip = form.udc_ip.data
        eapp.udc_username = form.udc_username.data
        eapp.udc_password = form.udc_password.data
        # eapp.root_username = form.root_username.data
        eapp.root_password = form.root_password.data
        # eapp.ubp_username = form.ubp_username.data
        eapp.ubp_password = form.ubp_password.data
        db.session.add(eapp)
        db.session.commit()
        flash('The eAPP has been updated')
        return redirect(url_for('.eapp'))
    form.mdc_ip.data = eapp.mdc_ip
    form.mdc_username.data = eapp.mdc_username
    form.mdc_password.data = eapp.mdc_password
    form.udc_ip.data = eapp.udc_ip
    form.udc_username.data = eapp.udc_username
    form.udc_password.data = eapp.udc_password
    # form.root_username.data = eapp.root_username
    form.root_password.data = eapp.root_password
    # form.ubp_username.data = eapp.ubp_username
    form.ubp_password.data = eapp.ubp_password
    return render_template('add_ecns.html', form=form)


@main.route('/delete-eapp/<int:id>', methods=['GET', 'POST'])
def delete_eapp(id):
    eapp = Eapp.query.get_or_404(id)
    db.session.delete(eapp)
    db.session.commit()
    return redirect(url_for('.eapp'))


@main.route('/enb', methods=['GET', 'POST'])
def enb():
    enbs = Enb.query.order_by(Enb.ip).all()
    # simulation_ecns = Ecns.query.filter(Ecns.usage == 'simulation').all()
    # simulation_num = len(simulation_ecns)
    # real_ecns = Ecns.query.filter(Ecns.usage == 'real').all()
    # real_num = len(real_ecns)
    return render_template('enb.html', enbs=enbs)


@main.route('/add-enb', methods=['GET', 'POST'])
def add_enb():
    form = EditeNBForm()
    if form.validate_on_submit():
        enb = Enb(ip=form.ip.data, username=form.username.data,
                  password=form.password.data, board=Board.query.get(form.board.data),
                  frequency=Frequency.query.get(form.frequency.data),
                  enb_id=form.enb_id.data, cell_id1=form.cell_id1.data, cell_id2=form.cell_id2.data)
        db.session.add(enb)
        db.session.commit()
        flash('Add enodeb successfully')
        return redirect(url_for('.enb'))
    return render_template('add_enb.html', form=form)


@main.route('/edit-enb/<int:id>', methods=['GET', 'POST'])
def edit_enb(id):
    enb = Enb.query.get_or_404(id)
    form = EditeNBForm()
    if form.validate_on_submit():
        enb.ip = form.ip.data
        enb.username = form.username.data
        enb.password = form.password.data
        enb.board = Board.query.get(form.board.data)
        enb.frequency = Frequency.query.get(form.frequency.data)
        enb.enb_id = form.enb_id.data
        enb.cell_id1 = form.cell_id1.data
        enb.cell_id2 = form.cell_id2.data
        db.session.add(enb)
        db.session.commit()
        flash('The enodeb has been updated')
        return redirect(url_for('.enb'))
    form.ip.data = enb.ip
    form.username.data = enb.username
    form.password.data = enb.password
    form.frequency.data = enb.frequency_id
    form.board.data = enb.board_id
    form.enb_id.data = enb.enb_id
    form.cell_id1 = enb.cell_id1
    form.cell_id2 = enb.cell_id2
    return render_template('add_enb.html', form=form)


@main.route('/delete-enb/<int:id>', methods=['GET', 'POST'])
def delete_enb(id):
    enb = Enb.query.get_or_404(id)
    db.session.delete(enb)
    db.session.commit()
    return redirect(url_for('.enb'))


@main.route('/add-ue', methods=['GET', 'POST'])
def add_ue():
    form = EditUEForm()
    if form.validate_on_submit():
        ue = UE(ue_model=UeModel.query.get(form.model.data), imsi=form.imsi.data, imei=form.imei.data,
                ki=form.ki.data, frequency=Frequency.query.get(form.frequency.data))
        db.session.add(ue)
        db.session.commit()
        flash('Add UE successfully')
        return redirect(url_for('.ue'))
    return render_template('add_ue.html', form=form)


@main.route('/ue', methods=['GET', 'POST'])
def ue():
    ues = UE.query.order_by(UE.frequency_id).all()
    # simulation_ecns = Ecns.query.filter(Ecns.usage == 'simulation').all()
    # simulation_num = len(simulation_ecns)
    # real_ecns = Ecns.query.filter(Ecns.usage == 'real').all()
    # real_num = len(real_ecns)
    return render_template('ue.html', ues=ues)


@main.route('/edit-ue/<int:id>', methods=['GET', 'POST'])
def edit_ue(id):
    ue = UE.query.get_or_404(id)
    form = EditUEForm()
    if form.validate_on_submit():
        ue.model = UeModel.query.get(form.model.data)
        ue.imsi = form.imsi.data
        ue.imei = form.imei.data
        ue.ki = form.ki.data
        ue.frequency = Frequency.query.get(form.frequency.data)
        db.session.add(ue)
        db.session.commit()
        flash('The enodeb has been updated')
        return redirect(url_for('.ue'))
    form.model.data = ue.ue_model_id
    form.imsi.data = ue.imsi
    form.imei.data = ue.imei
    form.ki.data = ue.ki
    form.frequency.data = ue.frequency_id
    return render_template('add_ue.html', form=form)


@main.route('/delete-ue/<int:id>', methods=['GET', 'POST'])
def delete_ue(id):
    ue = UE.query.get_or_404(id)
    db.session.delete(ue)
    db.session.commit()
    return redirect(url_for('.ue'))


@main.route('/add-ps-ue', methods=['GET', 'POST'])
def add_ps_ue():
    form = EditPsUeForm()
    if form.validate_on_submit():
        ps_ue = PsUe(ue_model=UeModel.query.get(form.model.data), imsi=form.imsi.data, imei=form.imei.data,
                     ki=form.ki.data, frequency=Frequency.query.get(form.frequency.data),
                     ip=form.ip.data, username=form.username.data, password=form.password.data)
        db.session.add(ps_ue)
        db.session.commit()
        flash('Add UE successfully')
        return redirect(url_for('.ps_ue'))
    return render_template('add_ps_ue.html', form=form)


@main.route('/ps-ue', methods=['GET', 'POST'])
def ps_ue():
    ps_ues = PsUe.query.order_by(PsUe.frequency_id).all()
    # simulation_ecns = Ecns.query.filter(Ecns.usage == 'simulation').all()
    # simulation_num = len(simulation_ecns)
    # real_ecns = Ecns.query.filter(Ecns.usage == 'real').all()
    # real_num = len(real_ecns)
    return render_template('ps_ue.html', ps_ues=ps_ues)


@main.route('/edit-ps-ue/<int:id>', methods=['GET', 'POST'])
def edit_ps_ue(id):
    ps_ue = PsUe.query.get_or_404(id)
    form = EditPsUeForm()
    if form.validate_on_submit():
        ps_ue.model = UeModel.query.get(form.model.data)
        ps_ue.imsi = form.imsi.data
        ps_ue.imei = form.imei.data
        ps_ue.ki = form.ki.data
        ps_ue.frequency = Frequency.query.get(form.frequency.data)
        ps_ue.ip = form.ip.data
        ps_ue.username = form.username.data
        ps_ue.password = form.password.data
        db.session.add(ps_ue)
        db.session.commit()
        flash('The enodeb has been updated')
        return redirect(url_for('.ue'))
    form.model.data = ps_ue.ue_model_id
    form.imsi.data = ps_ue.imsi
    form.imei.data = ps_ue.imei
    form.ki.data = ps_ue.ki
    form.frequency.data = ps_ue.frequency_id
    form.ip.data = ps_ue.ip
    form.username.data = ps_ue.username
    form.password.data = ps_ue.password
    return render_template('add_ps_ue.html', form=form)


@main.route('/delete-ps-ue/<int:id>', methods=['GET', 'POST'])
def delete_ps_ue(id):
    ps_ue = PsUe.query.get_or_404(id)
    db.session.delete(ps_ue)
    db.session.commit()
    return redirect(url_for('.ps_ue'))
