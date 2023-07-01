import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:netmanmain/data/device_group_data.dart';
import 'package:netmanmain/pages/devicegrouppage.dart';
import 'package:provider/provider.dart';

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  // _HomePageState() {
  //   _selectedValue = _dropDownItemsList[0];
  // }

  // @override
  // void initState() {
  //   super.initState();
  //
  //   Provider.of<DeviceGroupData>(context, listen: false)
  //       .initializeDeviceGroupList();
  // }

  // items for the dropdown box
  // final _dropDownItemsList = ["Router", "Switch", "Workstation", "Firewall"];
  // String _selectedValue = "";

  //text controller
  String deviceNameController = '';

  // text controller
  String communityStringController = '';

  // final newDeviceNameController = TextEditingController();
  String newDeviceIpAddressController = '';

  // String newDeviceGroupName = '';

  //
  // add new device and add to a device group
  void addDevice() {
    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        title: const Center(child: Text("Add a New Device")),
        content: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            // DropdownButton(
            //   value: _selectedValue,
            //   items: _dropDownItemsList
            //       .map(
            //         (e) => DropdownMenuItem(
            //           value: e,
            //           child: Text(e),
            //         ),
            //       )
            //       .toList(),
            //   onChanged: (val) {
            //     setState(() {
            //       _selectedValue = val!;
            //       newDeviceGroupName.text = val;
            //     });
            //   },
            //   icon: const Icon(
            //     Icons.arrow_drop_down_circle,
            //     color: Colors.blue,
            //   ),
            // ),
            //   community string
            TextField(
              decoration: const InputDecoration(hintText: "device name"),
              onChanged: (value){
                setState(() {
                  deviceNameController = value;
                });
              },
            ),
            TextField(
              decoration: const InputDecoration(hintText: "community string"),
              onChanged: (value) {
                setState(() {
                  communityStringController = value;
                });
              }
            ),
            TextField(
              decoration: const InputDecoration(hintText: "device ip address"),
              onChanged: (value){
                setState(() {
                  newDeviceIpAddressController = value;
                });
              },
            ),
          ],
        ),
        actions: [
          // add button
          MaterialButton(
            onPressed: save,
            child: const Text("Add"),
          ),

          // cancel button
          MaterialButton(
            onPressed: cancel,
            child: const Text("Cancel"),
          ),
        ],
      ),
    );
  }

  //get device address
  String getIp() {
    return newDeviceIpAddressController;
  }

  // save device
  void save() {
    //   get group name from text controller
    String groupName = deviceNameController;
    String communityString = communityStringController;
    String ipAddress = newDeviceIpAddressController;
    // Provider.of<D>(context)
  }

  // cancel device
  void cancel() {
    // pop dialog box
    Navigator.pop(context);
    clearController();
  }

  // clear controllers
  void clearController() {
    deviceNameController = "";
    communityStringController="";
    newDeviceIpAddressController="";
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: DefaultTabController(
        length: 4,
        child: Scaffold(
          extendBodyBehindAppBar: true,
          appBar: AppBar(
            title: const Text(
              'NetMan',
              style: TextStyle(letterSpacing: 10.0, wordSpacing: 2),
            ),
            // titleSpacing: 10.0,
            shape: const RoundedRectangleBorder(
                borderRadius:
                    BorderRadius.vertical(bottom: Radius.circular(20.0))),
            bottom: const TabBar(tabs: [
              Tab(
                text: "Topology",
                icon: Icon(Icons.hub_rounded),
              ),
              Tab(
                text: "Alerts",
                icon: Icon(Icons.notifications_rounded),
              ),
              Tab(
                text: "Statistics",
                icon: Icon(Icons.stacked_line_chart_rounded),
              ),
              Tab(
                text: "Devices",
                icon: Icon(Icons.devices_rounded),
              ),
            ]),
          ),
          body: TabBarView(children: [
            Container(
              color: Colors.white,
              child: Align(
                alignment: Alignment.bottomRight,
                child: Padding(
                  padding: const EdgeInsets.all(16.0),
                  child: FloatingActionButton(
                    onPressed: addDevice,
                    child: const Icon(Icons.add),
                  ),
                ),
              ),
            ),
            Container(
              color: Colors.white,
              child: const Center(
                child: Text(
                  'Tab 2 Content',
                  style: TextStyle(fontSize: 24),
                ),
              ),
            ),
            Container(
              color: Colors.white,
              child: const Center(
                child: Text(
                  'Tab 3 Content',
                  style: TextStyle(fontSize: 24),
                ),
              ),
            ),
            Container(
              color: Colors.white,
              child: Center(
                child: DeviceGroupPage(ipAddress: getIp(), groupName: deviceNameController),
              ),
            ),
          ]),
        ),
      ),
    );
  }
}
