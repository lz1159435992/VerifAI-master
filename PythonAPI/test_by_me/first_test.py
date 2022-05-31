import glob
import os
import sys
from PythonAPI.examples import dynamic_weather
try:
    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass
import time

import carla

import math
import random
def get_transform(vehicle_location, angle, d=6.4):
    a = math.radians(angle)
    location = carla.Location(d * math.cos(a), d * math.sin(a), 2.0) + vehicle_location
    return carla.Transform(location, carla.Rotation(yaw=180 + angle, pitch=-15))
def get_types_of_cars(blueprint_library):
    car_list = ['nissan', 'audi', 'bmw', 'chevrolet', 'citroen', 'dodge_charger', 'wrangler_rubicon', 'mercedes-benz',
                'cooperst', 'seat', 'toyota', 'model3', 'lincoln', 'mustang']
    car_blue_list = []
    car = []
    for i in car_list:
        car_blue_list.append(blueprint_library.filter(i))
    for i in car_blue_list:
        for j in i:
            car.append(j)
    bus = []
    for i in blueprint_library.filter('volkswagen'):
        bus.append(i)
    van = []
    for i in blueprint_library.filter('carlacola'):
        van.append(i)
    truck = []
    for i in blueprint_library.filter('cybertruck'):
        truck.append(i)
    bicycle_list = ['crossbike', 'omafiets', 'century']
    bicycle = []
    for i in bicycle_list:
        for j in blueprint_library.filter(i):
            bicycle.append(j)
    motorbicycle_list = ['harley-davidson', 'ninja', ' yamaha']
    motorbicycle = []
    for i in motorbicycle_list:
        for j in blueprint_library.filter(i):
            motorbicycle.append(j)
    return car,bus,van,truck,bicycle,motorbicycle
def main():
    actor_list = []
    #需要使用绝对路径加载地图
    #TOWN = 'E:/VerifAI-master/examples/carla/scenic/Town01'
    #TOWN = '/Game/Carla/Maps/Town04'
    TOWN = "D:\\carla\\WindowsNoEditor\\HDMaps\\Town03"
    #client = carla.Client('192.168.34.11', 2000)
    client = carla.Client('localhost',2000)
    client.set_timeout(5.0)
    print(client.get_available_maps())
    #open('D:/carla/WindowsNoEditor/HDMaps/Town03.pcd')
    #world = client.load_world(TOWN)

    world = client.get_world()
    weather = world.get_weather()
    print(weather)
    #world.set_weather(carla.WeatherParameters(float(50),float(50),float(50),float(50),float(50),float(50),float(50), float(50),float(50),float(50)))
    #world = client.load_world(TOWN)
    #world = client.load_world(client.get_available_maps()[0])
    #观察者，特殊actor，id=0，即是摄像机的位置
    spectator = world.get_spectator()
    #print(world.get_actors())
    # print(world.get_vehicles_light_states())
    blueprint_library = world.get_blueprint_library()
    car, bus, van, truck, bicycle, motorbicycle = get_types_of_cars(blueprint_library)
    # for i in blueprint_library:
    #     print(i.get_attribute('number_of_wheels'))
    #print(blueprint_library.filter('vehicle').type())
    vehicles = world.get_blueprint_library().filter("Harley")
    for i in vehicles:
        print(i)
    blueprint = random.choice(truck)
    #blueprint =  random.choice(blueprint_library.filter('trashcan03'))
    print(blueprint)
    if blueprint.has_attribute('color'):
        color = random.choice(blueprint.get_attribute('color').recommended_values)
        blueprint.set_attribute('color', color)

    print(blueprint)
    # vehicle_blueprints = world.get_blueprint_library().filter('vehicle')
    #
  # random.choice(world.get_map().get_spawn_points()) location 和 rocation组成的一对向量
    for i in world.get_map().get_spawn_points():
        print(i.location.x,i.location.y,i.location.z)
    location = random.choice(world.get_map().get_spawn_points()).location
    print(location.x,location.y,location.z)
    location = carla.Location(location.x+1.0,location.y+1.0,location.z +1.0)
    transform = carla.Transform(location, carla.Rotation(yaw=-45.0))
    #world.spawn_actor(blueprint, transform)
    vehicle = world.spawn_actor(blueprint, transform)
    #设置车辆的驾驶行为
    #vehicle.set_autopilot(True, client.get_trafficmanager(8000).get_port())
    vehicle.set_autopilot()
    # for i in range(10):
    #     vehicle.apply_control(carla.VehicleControl(throttle=1.0, steer=i/10))
    actor_list.append(vehicle)
    spectator.set_transform(get_transform(location,90))
    # print(vehicle.attributes)
    time.sleep(100)
    # transform = carla.Transform(random.choice(world.get_map().get_spawn_points()).location, carla.Rotation(yaw=-45.0))
    # vehicle.set_transform(transform)
    # spectator.set_transform(transform)
    #销毁actor
    for actor in actor_list:
        actor.destroy()
if __name__ == '__main__':

    main()
