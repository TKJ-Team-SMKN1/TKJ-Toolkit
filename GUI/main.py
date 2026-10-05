import sys

from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QGroupBox,
    QMessageBox,
)

from IPv4 import (
    validate_ip,
    validate_cidr,
    get_subnet,
    get_network_address,
    get_broadcast,
    get_usable_hosts,
    get_total_addresses,
)


class IPv4Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("TKJ Toolkit - IPv4 Calculator")
        self.setMinimumWidth(500)

        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        title = QLabel("TKJ Toolkit")
        title.setStyleSheet(
            "font-size: 24px; font-weight: bold;"
        )

        subtitle = QLabel("IPv4 Calculator")
        subtitle.setStyleSheet(
            "font-size: 16px;"
        )

        input_box = QGroupBox("Input")
        input_layout = QVBoxLayout()

        ip_layout = QHBoxLayout()
        ip_label = QLabel("IP Address:")
        self.ip_input = QLineEdit()
        self.ip_input.setPlaceholderText("192.168.1.10")

        ip_layout.addWidget(ip_label)
        ip_layout.addWidget(self.ip_input)

        cidr_layout = QHBoxLayout()
        cidr_label = QLabel("CIDR:")
        self.cidr_input = QLineEdit()
        self.cidr_input.setPlaceholderText("/24")

        cidr_layout.addWidget(cidr_label)
        cidr_layout.addWidget(self.cidr_input)

        input_layout.addLayout(ip_layout)
        input_layout.addLayout(cidr_layout)

        input_box.setLayout(input_layout)

        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.calculate)

        result_box = QGroupBox("Result")
        result_layout = QVBoxLayout()

        self.result_labels = {}

        results = [
            ("IP Address", "ip"),
            ("CIDR", "cidr"),
            ("Subnet Mask", "subnet"),
            ("Network Address", "network"),
            ("Broadcast", "broadcast"),
            ("First Usable Host", "first"),
            ("Last Usable Host", "last"),
            ("Usable Hosts", "usable"),
            ("Total Addresses", "total"),
        ]

        for label_text, key in results:
            row = QHBoxLayout()

            label = QLabel(f"{label_text}:")
            value = QLabel("-")

            value.setStyleSheet(
                "font-weight: bold;"
            )

            row.addWidget(label)
            row.addWidget(value)

            result_layout.addLayout(row)

            self.result_labels[key] = value

        result_box.setLayout(result_layout)

        main_layout.addWidget(title)
        main_layout.addWidget(subtitle)
        main_layout.addWidget(input_box)
        main_layout.addWidget(self.calculate_button)
        main_layout.addWidget(result_box)

        self.setLayout(main_layout)

    def calculate(self):
        try:
            ip = validate_ip(self.ip_input.text())
            cidr = validate_cidr(self.cidr_input.text())

            subnet = get_subnet(ip, cidr)
            network = get_network_address(ip, cidr)
            broadcast = get_broadcast(ip, cidr)
            hosts = get_usable_hosts(ip, cidr)
            total = get_total_addresses(ip, cidr)

            self.result_labels["ip"].setText(ip)
            self.result_labels["cidr"].setText(f"/{cidr}")
            self.result_labels["subnet"].setText(subnet)
            self.result_labels["network"].setText(network)
            self.result_labels["broadcast"].setText(broadcast)
            self.result_labels["first"].setText(hosts["first"])
            self.result_labels["last"].setText(hosts["last"])
            self.result_labels["usable"].setText(str(hosts["usable"]))
            self.result_labels["total"].setText(str(total))

        except ValueError as error:
            QMessageBox.warning(
                self,
                "Invalid Input",
                str(error),
            )


def main():
    app = QApplication(sys.argv)

    window = IPv4Calculator()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()