import 'package:flutter/cupertino.dart';
import 'package:netmanmain/models/devices.dart';

import '../models/device_groups.dart';
import '../models/interfaces.dart';
import '../models/router.dart';

class DeviceGroupData extends ChangeNotifier {
  // void createDeviceGroup() {
  //
  //
  //   //   Create instance of Device group and add devices
  // }

//  add a device group
  // create instances of interfaces

  // create instances of devices
  List<DeviceGroup> deviceGroupList = [
    //   default device group
    DeviceGroup(groupName: "Router", devicesList: [
      Device(
        deviceName: "Router1",
        memory: "75%",
        usedMemory: "35%",
        cpu: "50%",
        location: "London",
      ),
      Device(
        deviceName: "Router2",
        memory: "55%",
        usedMemory: "25%",
        cpu: "45%",
        location: "Birmingham",
      ),
    ]),
  ];

  // get the list of device groups
  List<DeviceGroup> getDeviceGroupList() {
    return deviceGroupList;
  }

  // get the number of devices in a group given device group name
  int numberOfDevicesInGroup(String deviceGroupName) {
    DeviceGroup relevantDeviceGroup = getRelevantDeviceGroup(deviceGroupName);


    return relevantDeviceGroup.devicesList.length;
  }

  // add a device group
  void addDeviceGroup(String name) {
    // add a new device group with a blank list of devices
    deviceGroupList.add(DeviceGroup(groupName: name, devicesList: []));
    notifyListeners();
  }

  // add a device to a group
  void addDevice(
      String deviceGroupName, deviceName, memory, usedMemory, cpu, location) {
    // find relevant device group
    DeviceGroup relevantDeviceGroup = getRelevantDeviceGroup(deviceGroupName);
    // then add a device to this workout
    relevantDeviceGroup.devicesList.add(Device(
        deviceName: deviceName,
        memory: memory,
        usedMemory: usedMemory,
        cpu: cpu,
        location: location));
    notifyListeners();
  }

  // return relevant device group object, given a device group name
  DeviceGroup getRelevantDeviceGroup(String deviceGroupName) {
    DeviceGroup relevantDeviceGroup = deviceGroupList
        .firstWhere((deviceGroup) => deviceGroup.groupName == deviceGroupName);
    return relevantDeviceGroup;
  }

  // return relevant device object, given a device group + exercise name
  Device getRelevantDevice(String deviceGroupName, String deviceName) {
    // find relevant device name first
    DeviceGroup relevantDeviceGroup = getRelevantDeviceGroup(deviceGroupName);
    // then find the relevant device in that device group
    Device relevantDevice = relevantDeviceGroup.devicesList
        .firstWhere((device) => device.deviceName == deviceName);
    return relevantDevice;
  }
}
