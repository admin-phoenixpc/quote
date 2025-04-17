@app.route("/api/builds", methods=["GET", "POST"])
def handle_builds():
    if request.method == "POST":
        form = request.json
        budget = str(form.get("budget"))
        builds = load_data()

        builds[budget] = {
            "Intel": {
                "CPU": form.get("intel_cpu"),
                "GPU": form.get("intel_gpu"),
                "RAM": form.get("intel_ram"),
                "SSD": form.get("intel_ssd"),
                "Cooler": form.get("intel_cooler"),
                "PSU": form.get("intel_psu"),
                "Case": form.get("intel_case"),
                "Note": form.get("intel_note"),
                "TotalPrice": sum([int(form.get(k, 0)) for k in [
                    "intel_cpu_price", "intel_gpu_price", "intel_ram_price",
                    "intel_ssd_price", "intel_cooler_price", "intel_psu_price", "intel_case_price"
                ]]),
                "TotalWatt": sum([int(form.get(k, 0)) for k in [
                    "intel_cpu_watt", "intel_gpu_watt", "intel_ram_watt",
                    "intel_ssd_watt", "intel_cooler_watt"
                ]])
            },
            "AMD": {
                "CPU": form.get("amd_cpu"),
                "GPU": form.get("amd_gpu"),
                "RAM": form.get("amd_ram"),
                "SSD": form.get("amd_ssd"),
                "Cooler": form.get("amd_cooler"),
                "PSU": form.get("amd_psu"),
                "Case": form.get("amd_case"),
                "Note": form.get("amd_note"),
                "TotalPrice": sum([int(form.get(k, 0)) for k in [
                    "amd_cpu_price", "amd_gpu_price", "amd_ram_price",
                    "amd_ssd_price", "amd_cooler_price", "amd_psu_price", "amd_case_price"
                ]]),
                "TotalWatt": sum([int(form.get(k, 0)) for k in [
                    "amd_cpu_watt", "amd_gpu_watt", "amd_ram_watt",
                    "amd_ssd_watt", "amd_cooler_watt"
                ]])
            }
        }

        save_data(builds)
        return jsonify({"status": "saved"})

    return jsonify(load_data())
