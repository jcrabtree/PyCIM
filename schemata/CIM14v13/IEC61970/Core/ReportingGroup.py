# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA

from CIM14v13.IEC61970.Core.IdentifiedObject import IdentifiedObject

class ReportingGroup(IdentifiedObject):
    """A reporting group is used for various ad-hoc groupings used for reporting.
    """

    def __init__(self, TopologicalNode=None, BusNameMarker=None, PowerSystemResource=None, ReportingSuperGroup=None, *args, **kw_args):
        """Initializes a new 'ReportingGroup' instance.

        @param TopologicalNode: The topological nodes that belong to the reporting group.
        @param BusNameMarker: The BusNameMarkers that belong to this reporting group.
        @param PowerSystemResource: PSR's which belong to this reporting group.
        @param ReportingSuperGroup: Reporting super group to which this reporting group belongs.
        """
        self._TopologicalNode = []
        self.TopologicalNode = [] if TopologicalNode is None else TopologicalNode

        self._BusNameMarker = []
        self.BusNameMarker = [] if BusNameMarker is None else BusNameMarker

        self._PowerSystemResource = []
        self.PowerSystemResource = [] if PowerSystemResource is None else PowerSystemResource

        self._ReportingSuperGroup = None
        self.ReportingSuperGroup = ReportingSuperGroup

        super(ReportingGroup, self).__init__(*args, **kw_args)

    def getTopologicalNode(self):
        """The topological nodes that belong to the reporting group.
        """
        return self._TopologicalNode

    def setTopologicalNode(self, value):
        for x in self._TopologicalNode:
            x._ReportingGroup = None
        for y in value:
            y._ReportingGroup = self
        self._TopologicalNode = value

    TopologicalNode = property(getTopologicalNode, setTopologicalNode)

    def addTopologicalNode(self, *TopologicalNode):
        for obj in TopologicalNode:
            obj._ReportingGroup = self
            self._TopologicalNode.append(obj)

    def removeTopologicalNode(self, *TopologicalNode):
        for obj in TopologicalNode:
            obj._ReportingGroup = None
            self._TopologicalNode.remove(obj)

    def getBusNameMarker(self):
        """The BusNameMarkers that belong to this reporting group.
        """
        return self._BusNameMarker

    def setBusNameMarker(self, value):
        for x in self._BusNameMarker:
            x._ReportingGroup = None
        for y in value:
            y._ReportingGroup = self
        self._BusNameMarker = value

    BusNameMarker = property(getBusNameMarker, setBusNameMarker)

    def addBusNameMarker(self, *BusNameMarker):
        for obj in BusNameMarker:
            obj._ReportingGroup = self
            self._BusNameMarker.append(obj)

    def removeBusNameMarker(self, *BusNameMarker):
        for obj in BusNameMarker:
            obj._ReportingGroup = None
            self._BusNameMarker.remove(obj)

    def getPowerSystemResource(self):
        """PSR's which belong to this reporting group.
        """
        return self._PowerSystemResource

    def setPowerSystemResource(self, value):
        for p in self._PowerSystemResource:
            filtered = [q for q in p.ReportingGroup if q != self]
            self._PowerSystemResource._ReportingGroup = filtered
        for r in value:
            if self not in r._ReportingGroup:
                r._ReportingGroup.append(self)
        self._PowerSystemResource = value

    PowerSystemResource = property(getPowerSystemResource, setPowerSystemResource)

    def addPowerSystemResource(self, *PowerSystemResource):
        for obj in PowerSystemResource:
            if self not in obj._ReportingGroup:
                obj._ReportingGroup.append(self)
            self._PowerSystemResource.append(obj)

    def removePowerSystemResource(self, *PowerSystemResource):
        for obj in PowerSystemResource:
            if self in obj._ReportingGroup:
                obj._ReportingGroup.remove(self)
            self._PowerSystemResource.remove(obj)

    def getReportingSuperGroup(self):
        """Reporting super group to which this reporting group belongs.
        """
        return self._ReportingSuperGroup

    def setReportingSuperGroup(self, value):
        if self._ReportingSuperGroup is not None:
            filtered = [x for x in self.ReportingSuperGroup.ReportingGroup if x != self]
            self._ReportingSuperGroup._ReportingGroup = filtered

        self._ReportingSuperGroup = value
        if self._ReportingSuperGroup is not None:
            self._ReportingSuperGroup._ReportingGroup.append(self)

    ReportingSuperGroup = property(getReportingSuperGroup, setReportingSuperGroup)
