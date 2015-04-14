from pro import *

from lib.metro import *

height = param(10)
entranceWidth = param(6)


@rule
def Begin():
	StationHall(height, Wall(), Wall(), Side(), Side(), Platform())


@rule
def Platform():
	texture("MarekFootway0007.jpg", 0.6, 0.3)
	split(y,
		3,
		3 >> Columns(),
		flt(),
		3 >> Columns(),
		3
	)


@rule
def Columns():
	split(x,
		4,
		repeat(
			3 >> Column(),
			flt(4)
		),
		4
	)


@rule
def Column():
	texture("platform_wall.jpg", 1.4, 0.7)
	extrude(8)


@rule
def Wall():
	texture("platform_wall.jpg", 14, 7)
	split(y,
		rel(0.3),
		flt() >> extrude(0.4)
	)


@rule
def Side():
	split(x,
		flt(),
		rel(0.8) >> split(y,
			platformHeight >> delete(),
			rel(0.6) >> EntranceToPlatform(),
			flt() >> delete()
		),
		flt()
	)


@rule
def EntranceToPlatform():
	extrude2(
		0, -20 >> delete(),
		1.6, -20 >> split(y,
			flt() >> Steps(20),
			3 >> extrude(-20, top >> delete(), front >> PedestrianSubway())
		),
		1.6, -10 >> delete(),
		last >> delete(),
		axis = y,
		symmetric = False
	)


@rule
def PedestrianSubway():
	texture("pedestrian_subway_wall.jpg", 0.8, 0.8)
	extrude2(
		-60, 3,
		-60, 64,
		-66, 64 >> Entrance(10, 5, 5),
		-66, -3,
		60, -7 >> split(x,
			33.8,
			entranceWidth >> Entrance(),
			40,
			entranceWidth >> Entrance(),
			flt(),
			entranceWidth >> Entrance(),
			7.5
		),
		62, 88,
		55, 88,
		53, -1,
		last >> delete(),
		cap2 >> delete(),
		cap1 >> texture("MarekFootway0007.jpg", 0.6, 0.3),
		symmetric = False,
		relativeCoord1 = False
	)
