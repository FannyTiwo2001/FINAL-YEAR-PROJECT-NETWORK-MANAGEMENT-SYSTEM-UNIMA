import 'package:flutter/material.dart';
import 'package:netmanmain/data/device_group_data.dart';
import 'package:netmanmain/pages/devicespage.dart';
import 'package:get/get.dart';
import 'package:provider/provider.dart';

import '../components/device_card_view.dart';

class DeviceGroupPage extends StatefulWidget {
  final String ipAddress;
  final String groupName;

  const DeviceGroupPage({
    super.key,
    required this.ipAddress, required this.groupName,
  });

  @override
  State<DeviceGroupPage> createState() => _DeviceGroupPageState();
}

class _DeviceGroupPageState extends State<DeviceGroupPage> {
  // @override
  // void iniState() {
  //   super.initState();
  //   Provider.of<DeviceGroupData>(context, listen: false);
  // }

  List<String> imageList = [
    'lib/images/router7435.png',
    'lib/images/workgroup-switch.png',
    'lib/images/workstation.png',
    'lib/images/firewall.png'
  ];

  List<String> namesList = ['Routers', 'Switch', 'Workstations', 'Firewalls'];

  // void goToDevicesPage(String groupName) {
  //   Navigator.push(
  //     context,
  //     MaterialPageRoute(
  //       builder: (context) => DeviceView(
  //         deviceGroupName: groupName,
  //       ),
  //     ),
  //   );
  // }

  @override
  Widget build(BuildContext context) {
    return Container(
      height: double.infinity,
      width: double.infinity,
      color: Colors.white54,
      child: SafeArea(
          child: Container(
        padding: const EdgeInsets.all(20.0),
        child: Column(
          children: [
            Container(
              width: double.infinity,
              height: 150,
              decoration: BoxDecoration(
                  borderRadius: BorderRadius.circular(20),
                  image: const DecorationImage(
                    image: AssetImage("lib/images/gateway.jpg"),
                    fit: BoxFit.cover,
                  )),
              child: Container(
                decoration: BoxDecoration(
                    borderRadius: BorderRadius.circular(20),
                    gradient: LinearGradient(
                        begin: Alignment.bottomRight,
                        colors: [
                          Colors.black.withOpacity(.4),
                          Colors.black.withOpacity(.5)
                        ])),
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: const [
                    Text(
                      "Devices",
                      style: TextStyle(
                          color: Colors.white,
                          fontSize: 40,
                          fontWeight: FontWeight.bold),
                    )
                  ],
                ),
              ),
            ),
            const SizedBox(
              height: 40,
            ),
            Expanded(
              child: GridView.builder(
                  itemCount: imageList.length,
                  gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
                      crossAxisSpacing: 10,
                      mainAxisSpacing: 10,
                      crossAxisCount: 2),
                  itemBuilder: (context, index) {
                    return Padding(
                      padding: const EdgeInsets.all(8.0),
                      child: GestureDetector(
                        onTap: () {
                          // Get.to(() => const DeviceView(),
                          //     transition: Transition.rightToLeft);
                          for (String name in [namesList[index]]) {
                            if (name == 'Routers') {
                              Navigator.push(
                                  context,
                                  MaterialPageRoute(
                                      builder: (context) => DeviceView(
                                          myIPAddress: widget.ipAddress,deviceGroupName: widget.groupName,)));

                              // goToDevicesPage(name);
                            }
                          }
                        },
                        child: DeviceCardView(groupName: widget.groupName,
                            images: [imageList[index]],
                            names: [namesList[index]]),
                      ),
                    );
                  }),
            ),
          ],
        ),
      )),
    );
  }
}
