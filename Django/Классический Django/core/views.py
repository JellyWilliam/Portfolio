from datetime import datetime
from django.shortcuts import render

from copy import deepcopy

from .moduls.tarif_calc import tarif_calc, get_detail_improvement
from .moduls.tarif_obr import tarif_obr, provision_detail


def test(request):
    summ = 0
    if request.method == "POST":
        print(request.POST)
        address = request.POST["address"]
        company = request.POST["company"]
        # date = request.POST["date"]
        boardSize = float(request.POST["boardSize"])
        totalArea = float(request.POST["totalArea"])
        areaResidential = float(request.POST["areaResidential"])
        floor = float(request.POST["floor"])
        yearCommissioning = float(request.POST["yearCommissioning"])
        walls = float(request.POST["walls"])
        improvement = request.POST["improvement[]"]

        arr, summ = tarif_calc(
            boardSize,
            totalArea,
            areaResidential,
            floor,
            yearCommissioning,
            walls,
            get_detail_improvement(improvement),
        )
        return render(
            request,
            "test.html",
            {
                "date": datetime.today().strftime("%d.%m.%Y"),
                "sum": summ,
                "year_now": int(datetime.today().strftime("%Y")),
            },
        )
    else:
        return render(
            request,
            "test.html",
            {
                "date": datetime.today().strftime("%d.%m.%Y"),
                "sum": summ,
                "year_now": int(datetime.today().strftime("%Y")),
            },
        )


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def news(request):
    return render(request, "news.html")


def personal_areal(request):
    return render(request, "personal_areal.html")


def tarif(request):
    if request.method == "POST":
        if "Detail" in request.POST:
            print(request.POST)
            address = request.POST["d-address"]
            company = request.POST["d-company"]
            # date = request.POST["date"]
            boardSize = float(request.POST["d-boardSize"])
            totalArea = float(request.POST["d-totalArea"])
            areaResidential = float(request.POST["d-areaResidential"])
            floor = float(request.POST["d-floor"])
            yearCommissioning = float(request.POST["d-yearCommissioning"])
            walls = float(request.POST["d-walls"])
            improvement = request.POST.getlist("d-improvement[]")
            arr, summ = tarif_calc(
                boardSize,
                totalArea,
                areaResidential,
                floor,
                yearCommissioning,
                walls,
                get_detail_improvement(improvement),
            )
            print(address)
            return render(
                request,
                "tarif.html",
                {
                    "date": datetime.today().strftime("%d.%m.%Y"),
                    "year_now": int(datetime.today().strftime("%Y")),
                    # Для детализации
                    "d_address": address,
                    "d_company": company,
                    "d_boardSize": str(boardSize),
                    "d_totalArea": str(totalArea)[:-2],
                    "d_areaResidential": str(areaResidential)[:-2],
                    "d_floor": str(floor)[:-2],
                    "d_yearCommissioning": str(yearCommissioning)[:-2],
                    "d_arr": arr,
                    "d_sum": boardSize,
                    "d_sum_square": boardSize * totalArea,
                    "d_sum_year": boardSize * totalArea * 12,
                    "d_hidden": True,
                    # Для расчета
                    "c_address": "",
                    "c_company": "",
                    "c-year": 1980,
                    "c-floor_all": "",
                    "c-floor_underground": "",
                    "c-entrances": "",
                    "c-apartments": "",
                    "c-residents": "",
                    "c-area_all": "",
                    "c-area_resident": "",
                    "c-area_attic": "",
                    "c-area_basement": "",
                    "c-area_land_mar": "",
                    "c-n_gar_chute": "",
                    "c-elevators": "",
                    "c-area_elevator": "",
                    "c_rate_ret": "",
                    "c_base_lift": "",
                    "c_mrot": 13890,
                    "c_hidden": False,
                },
            )
        elif "Calculate" in request.POST:
            year = int(request.POST["c-year"])
            floor_all = int(request.POST["c-floor_all"])
            floor_underground = int(request.POST["c-floor_underground"])
            entrances = int(request.POST["c-entrances"])
            apartments = int(request.POST["c-apartments"])
            residents = int(request.POST["c-residents"])
            area_all = float(request.POST["c-area_all"])
            area_resident = float(request.POST["c-area_resident"])
            area_attic = float(request.POST["c-area_attic"])
            area_basement = float(request.POST["c-area_basement"])
            area_land_mar = float(request.POST["c-area_land_mar"])
            n_gar_chute = int(request.POST["c-n_gar_chute"])
            elevators = int(request.POST["c-elevators"])
            area_elevator = float(request.POST["c-area_elevator"])
            type_exterior_wall = int(request.POST["c-type_exterior_wall"])
            type_found = int(request.POST["c-type_found"])
            type_overlap = int(request.POST["c-type_overlap"])
            services = request.POST.getlist("c-services[]")
            rate_ret = float(request.POST["c-rate_ret"])
            base_lift = float(request.POST["c-base_lift"])
            provision = request.POST.getlist("c-provision[]")
            heating, aogv, supply_hot, supply_cold, drainage, supply_gas = provision_detail(provision)

            boardSize = tarif_obr(
                year, floor_all, floor_underground, entrances, apartments, residents, area_all, area_resident,
                area_attic, area_basement, area_land_mar, n_gar_chute, elevators, area_elevator, type_exterior_wall,
                type_found, type_overlap, heating, aogv, supply_hot, supply_cold, drainage, supply_gas, services,
                rate_ret, base_lift
            )
            # arr, summ = tarif_calc(
            #     c_boardSize,
            #     area_all,
            #     area_resident,
            #     floor_all - floor_underground,
            #     year,
            #     walls,
            #     get_detail_improvement(improvement),
            # )

            return render(
                request,
                "tarif.html",
                {
                    "date": datetime.today().strftime("%d.%m.%Y"),
                    "year_now": int(datetime.today().strftime("%Y")),
                    # Для детализации
                    "d_sum": "",
                    "d_sum_square": "",
                    "d_sum_year": "",
                    "d_address": "",
                    "d_company": "",
                    "d_boardSize": "",
                    "d_totalArea": "",
                    "d_areaResidential": "",
                    "d_floor": "",
                    "d_yearCommissioning": 1980,
                    "d_arr": [],
                    "d_hidden": False,
                    # Для расчета
                    "c_address": request.POST["c-adress"],
                    "c_company": request.POST["c-company"],
                    "c_year": 1980,
                    "c_floor_all": floor_all,
                    "c_floor_underground": floor_underground,
                    "c_entrances": entrances,
                    "c_apartments": apartments,
                    "c_residents": residents,
                    "c_area_all": area_all,
                    "c_area_resident": area_resident,
                    "c_area_attic": area_attic,
                    "c_area_basement": area_basement,
                    "c_area_land_mar": area_land_mar,
                    "c_n_gar_chute": n_gar_chute,
                    "c_elevators": elevators,
                    "c_area_elevator": area_elevator,
                    "c_rate_ret": rate_ret,
                    "c_base_lift": base_lift,
                    "c_mrot": 13890,
                    "c_boardSize": boardSize,
                    "c_arr": [],
                    "c_hidden": True,
                },
            )
    else:
        return render(
            request,
            "tarif.html",
            {
                "date": datetime.today().strftime("%d.%m.%Y"),
                "year_now": int(datetime.today().strftime("%Y")),
                # Для детализации
                "d_sum": "",
                "d_sum_square": "",
                "d_sum_year": "",
                "d_address": "",
                "d_company": "",
                "d_boardSize": 0,
                "d_totalArea": 0,
                "d_areaResidential": 0,
                "d_floor": 0,
                "d_yearCommissioning": 1980,
                "d_arr": [],
                "d_hidden": False,
                # Для расчета
                "c_address": "",
                "c_company": "",
                "c-year": 1980,
                "c-floor_all": "",
                "c-floor_underground": "",
                "c-entrances": "",
                "c-apartments": "",
                "c-residents": "",
                "c-area_all": "",
                "c-area_resident": "",
                "c-area_attic": "",
                "c-area_basement": "",
                "c-area_land_mar": "",
                "c-n_gar_chute": "",
                "c-elevators": "",
                "c-area_elevator": "",
                "c_rate_ret": "",
                "c_base_lift": "",
                "c_mrot": 13890,
                "c_arr": [],
                "c_hidden": False,
            },
        )
