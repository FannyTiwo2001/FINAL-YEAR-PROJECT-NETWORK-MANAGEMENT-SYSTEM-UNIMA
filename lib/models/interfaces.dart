class Interfaces {
  final String ipAddress;
  final String trafficIn;
  final String trafficOut;
  final String administrativeStatus;
  final String operationalStatus;
  final String bandwidth;

  Interfaces(
      {required this.ipAddress,
      required this.trafficIn,
      required this.trafficOut,
      required this.administrativeStatus,
      required this.operationalStatus,
      required this.bandwidth});
}
