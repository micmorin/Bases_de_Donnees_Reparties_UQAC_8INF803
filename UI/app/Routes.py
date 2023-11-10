from flask import Blueprint
import Controller

route_main = Blueprint('main',__name__, url_prefix="/")

route_main.route("/",                       methods=['GET', 'POST'])(Controller.main_index)
route_main.route("/login",                  methods=['GET', 'POST'])(Controller.main_login)
route_main.route("/logout"                                         )(Controller.main_logout)

route_user = Blueprint('user', __name__,url_prefix="/user")

route_user.route('/personnel/',           methods=['GET', 'POST'])        (Controller.personnel)
route_user.route('/palmares/',            methods=['GET', 'POST'])        (Controller.palmares)
route_user.route('/calendrier',           methods=['GET', 'POST'])        (Controller.calendrier)
route_user.route('/matchs',               methods=['GET', 'POST'])        (Controller.match)
route_user.route('/staffTechnique',       methods=['GET', 'POST'])        (Controller.stafftechnique)
route_user.route('/equipes',              methods=['GET', 'POST'])        (Controller.equipe)
route_user.route('/joueurs',              methods=['GET', 'POST'])        (Controller.joueur)
route_user.route('/stades',               methods=['GET', 'POST'])        (Controller.stade)

route_user.route('/bureau',                 methods=['GET', 'POST'])        (Controller.bureau)
route_user.route('/arbitre',                methods=['GET', 'POST'])        (Controller.arbitre)
route_user.route('/dirigeant',              methods=['GET', 'POST'])        (Controller.dirigeant)
route_user.route('/statistique_spectateur', methods=['GET', 'POST'])        (Controller.statistique_spectateur)
route_user.route('/statistique_buts',         methods=['GET', 'POST'])      (Controller.statistique_buts)
route_user.route('/statistique_resultat_match', methods=['GET', 'POST'])      (Controller.statistique_resultat_match)
route_user.route('/statistique_palmares',     methods=['GET', 'POST'])        (Controller.statistique_palmares)

route_user.route('/palmaresGlobal',         methods=['GET', 'POST'])        (Controller.palmares_Global)
route_user.route('/calendrierGlobal',       methods=['GET', 'POST'])        (Controller.calendrier_Global)
route_user.route('/clubGlobal',             methods=['GET', 'POST'])        (Controller.club_global)
route_user.route('/joueurGlobal',           methods=['GET', 'POST'])        (Controller.joueur_global)
route_user.route('/matchGlobal',            methods=['GET', 'POST'])        (Controller.match_global)
route_user.route('personnelGlobal',         methods=['GET', 'POST'])        (Controller.personnel_global)
route_user.route('staffTechniqueGlobal',    methods=['GET', 'POST'])        (Controller.staff_technique_global)
route_user.route('stadeGlobal',             methods=['GET', 'POST'])        (Controller.stade_global)