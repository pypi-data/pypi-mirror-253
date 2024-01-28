from __future__ import annotations

from enum import Enum
from typing import Optional

__doc__: str
__version__: str

class AirState:
    OnGround = 0
    Jumping = 1
    DoubleJumping = 2
    Dodging = 3
    InAir = 4

    def __init__(self, value: int = 0): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> AirState: ...

class BallBouncinessOption:
    Default = 0
    Low = 1
    High = 2
    Super_High = 3

    def __init__(self, value: int = 0): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> BallBouncinessOption: ...

class BallInfo:
    physics: Physics
    latest_touch: Touch
    shape: CollisionShape

    def __init__(
        self,
        physics=Physics(),
        latest_touch=Touch(),
        shape=CollisionShape(),
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> BallInfo: ...

class BallMaxSpeedOption:
    Default = 0
    Slow = 1
    Fast = 2
    Super_Fast = 3

    def __init__(self, value: int = 0): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> BallMaxSpeedOption: ...

class BallPrediction:
    slices: list[PredictionSlice]

    def __init__(
        self,
        slices=[],
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> BallPrediction: ...

class BallSizeOption:
    Default = 0
    Small = 1
    Large = 2
    Gigantic = 3

    def __init__(self, value: int = 0): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> BallSizeOption: ...

class BallTypeOption:
    Default = 0
    Cube = 1
    Puck = 2
    Basketball = 3

    def __init__(self, value: int = 0): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> BallTypeOption: ...

class BallWeightOption:
    Default = 0
    Light = 1
    Heavy = 2
    Super_Light = 3

    def __init__(self, value: int = 0): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> BallWeightOption: ...

class Bool:
    val: bool

    def __init__(
        self,
        val=False,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> Bool: ...

class BoostOption:
    Normal_Boost = 0
    Unlimited_Boost = 1
    Slow_Recharge = 2
    Rapid_Recharge = 3
    No_Boost = 4

    def __init__(self, value: int = 0): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> BoostOption: ...

class BoostPad:
    location: Vector3
    is_full_boost: bool

    def __init__(
        self,
        location=Vector3(),
        is_full_boost=False,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> BoostPad: ...

class BoostPadState:
    is_active: bool
    timer: float

    def __init__(
        self,
        is_active=False,
        timer=0,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> BoostPadState: ...

class BoostStrengthOption:
    One = 0
    OneAndAHalf = 1
    Two = 2
    Ten = 3

    def __init__(self, value: int = 0): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> BoostStrengthOption: ...

class BoxShape:
    length: float
    width: float
    height: float

    def __init__(
        self,
        length=0,
        width=0,
        height=0,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> BoxShape: ...

class CollisionShapeType(Enum):
    NONE = 0
    BoxShape = 1
    SphereShape = 2
    CylinderShape = 3

class CollisionShape:
    item_type: CollisionShapeType
    box_shape: Optional[BoxShape]
    sphere_shape: Optional[SphereShape]
    cylinder_shape: Optional[CylinderShape]

    def __init__(
        self,
        box_shape=None,
        sphere_shape=None,
        cylinder_shape=None,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...

class Color:
    a: int
    r: int
    g: int
    b: int

    def __init__(
        self,
        a=0,
        r=0,
        g=0,
        b=0,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> Color: ...

class ConsoleCommand:
    command: str

    def __init__(
        self,
        command="",
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> ConsoleCommand: ...

class ControllerState:
    throttle: float
    steer: float
    pitch: float
    yaw: float
    roll: float
    jump: bool
    boost: bool
    handbrake: bool
    use_item: bool

    def __init__(
        self,
        throttle=0,
        steer=0,
        pitch=0,
        yaw=0,
        roll=0,
        jump=False,
        boost=False,
        handbrake=False,
        use_item=False,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> ControllerState: ...

class CylinderShape:
    diameter: float
    height: float

    def __init__(
        self,
        diameter=0,
        height=0,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> CylinderShape: ...

class DemolishOption:
    Default = 0
    Disabled = 1
    Friendly_Fire = 2
    On_Contact = 3
    On_Contact_FF = 4

    def __init__(self, value: int = 0): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> DemolishOption: ...

class DesiredBallState:
    physics: DesiredPhysics

    def __init__(
        self,
        physics=DesiredPhysics(),
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> DesiredBallState: ...

class DesiredBoostState:
    respawn_time: Optional[Float]

    def __init__(
        self,
        respawn_time=None,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> DesiredBoostState: ...

class DesiredCarState:
    physics: Optional[DesiredPhysics]
    boost_amount: Optional[Float]

    def __init__(
        self,
        physics=None,
        boost_amount=None,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> DesiredCarState: ...

class DesiredGameInfoState:
    world_gravity_z: Optional[Float]
    game_speed: Optional[Float]
    paused: Optional[Bool]
    end_match: Optional[Bool]

    def __init__(
        self,
        world_gravity_z=None,
        game_speed=None,
        paused=None,
        end_match=None,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> DesiredGameInfoState: ...

class DesiredGameState:
    ball_state: Optional[DesiredBallState]
    car_states: list[DesiredCarState]
    boost_states: list[DesiredBoostState]
    game_info_state: Optional[DesiredGameInfoState]
    console_commands: list[ConsoleCommand]

    def __init__(
        self,
        ball_state=None,
        car_states=[],
        boost_states=[],
        game_info_state=None,
        console_commands=[],
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> DesiredGameState: ...

class DesiredPhysics:
    location: Optional[Vector3Partial]
    rotation: Optional[RotatorPartial]
    velocity: Optional[Vector3Partial]
    angular_velocity: Optional[Vector3Partial]

    def __init__(
        self,
        location=None,
        rotation=None,
        velocity=None,
        angular_velocity=None,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> DesiredPhysics: ...

class ExistingMatchBehavior:
    Restart_If_Different = 0
    Restart = 1
    Continue_And_Spawn = 2

    def __init__(self, value: int = 0): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> ExistingMatchBehavior: ...

class FieldInfo:
    boost_pads: list[BoostPad]
    goals: list[GoalInfo]

    def __init__(
        self,
        boost_pads=[],
        goals=[],
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> FieldInfo: ...

class Float:
    val: float

    def __init__(
        self,
        val=0,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> Float: ...

class GameInfo:
    seconds_elapsed: float
    game_time_remaining: float
    is_overtime: bool
    is_unlimited_time: bool
    game_state_type: GameStateType
    world_gravity_z: float
    game_speed: float
    frame_num: int

    def __init__(
        self,
        seconds_elapsed=0,
        game_time_remaining=0,
        is_overtime=False,
        is_unlimited_time=False,
        game_state_type=GameStateType(),
        world_gravity_z=0,
        game_speed=0,
        frame_num=0,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> GameInfo: ...

class GameMessageType(Enum):
    NONE = 0
    PlayerStatEvent = 1
    PlayerSpectate = 2
    PlayerInputChange = 3

class GameMessage:
    item_type: GameMessageType
    player_stat_event: Optional[PlayerStatEvent]
    player_spectate: Optional[PlayerSpectate]
    player_input_change: Optional[PlayerInputChange]

    def __init__(
        self,
        player_stat_event=None,
        player_spectate=None,
        player_input_change=None,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...

class GameMessageWrapper:
    message: GameMessage

    def __init__(
        self,
        message=GameMessage(),
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> GameMessageWrapper: ...

class GameMode:
    Soccer = 0
    Hoops = 1
    Dropshot = 2
    Hockey = 3
    Rumble = 4
    Heatseeker = 5
    Gridiron = 6

    def __init__(self, value: int = 0): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> GameMode: ...

class GameSpeedOption:
    Default = 0
    Slo_Mo = 1
    Time_Warp = 2

    def __init__(self, value: int = 0): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> GameSpeedOption: ...

class GameStateType:
    Inactive = 0
    Countdown = 1
    Kickoff = 2
    Active = 3
    GoalScored = 4
    Replay = 5
    Paused = 6
    Ended = 7

    def __init__(self, value: int = 0): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> GameStateType: ...

class GameTickPacket:
    players: list[PlayerInfo]
    boost_pad_states: list[BoostPadState]
    ball: BallInfo
    game_info: GameInfo
    teams: list[TeamInfo]

    def __init__(
        self,
        players=[],
        boost_pad_states=[],
        ball=BallInfo(),
        game_info=GameInfo(),
        teams=[],
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> GameTickPacket: ...

class GoalInfo:
    team_num: int
    location: Vector3
    direction: Vector3
    width: float
    height: float

    def __init__(
        self,
        team_num=0,
        location=Vector3(),
        direction=Vector3(),
        width=0,
        height=0,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> GoalInfo: ...

class GravityOption:
    Default = 0
    Low = 1
    High = 2
    Super_High = 3

    def __init__(self, value: int = 0): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> GravityOption: ...

class HumanPlayer:

    def __init__(
        self,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> HumanPlayer: ...

class Launcher:
    Steam = 0
    Epic = 1
    Custom = 2

    def __init__(self, value: int = 0): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> Launcher: ...

class Line3D:
    color: Color
    start: Vector3
    end: Vector3

    def __init__(
        self,
        color=Color(),
        start=Vector3(),
        end=Vector3(),
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> Line3D: ...

class LoadoutPaint:
    car_paint_id: int
    decal_paint_id: int
    wheels_paint_id: int
    boost_paint_id: int
    antenna_paint_id: int
    hat_paint_id: int
    trails_paint_id: int
    goal_explosion_paint_id: int

    def __init__(
        self,
        car_paint_id=0,
        decal_paint_id=0,
        wheels_paint_id=0,
        boost_paint_id=0,
        antenna_paint_id=0,
        hat_paint_id=0,
        trails_paint_id=0,
        goal_explosion_paint_id=0,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> LoadoutPaint: ...

class MatchLength:
    Five_Minutes = 0
    Ten_Minutes = 1
    Twenty_Minutes = 2
    Unlimited = 3

    def __init__(self, value: int = 0): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> MatchLength: ...

class MatchSettings:
    launcher: Launcher
    game_path: str
    auto_start_bots: bool
    player_configurations: list[PlayerConfiguration]
    game_mode: GameMode
    skip_replays: bool
    instant_start: bool
    mutator_settings: Optional[MutatorSettings]
    existing_match_behavior: ExistingMatchBehavior
    enable_rendering: bool
    enable_state_setting: bool
    auto_save_replay: bool
    game_map_upk: str

    def __init__(
        self,
        launcher=Launcher(),
        game_path="",
        auto_start_bots=False,
        player_configurations=[],
        game_mode=GameMode(),
        skip_replays=False,
        instant_start=False,
        mutator_settings=None,
        existing_match_behavior=ExistingMatchBehavior(),
        enable_rendering=False,
        enable_state_setting=False,
        auto_save_replay=False,
        game_map_upk="",
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> MatchSettings: ...

class MaxScore:
    Unlimited = 0
    One_Goal = 1
    Three_Goals = 2
    Five_Goals = 3

    def __init__(self, value: int = 0): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> MaxScore: ...

class MessagePacket:
    messages: list[GameMessageWrapper]
    game_seconds: float
    frame_num: int

    def __init__(
        self,
        messages=[],
        game_seconds=0,
        frame_num=0,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> MessagePacket: ...

class MutatorSettings:
    match_length: MatchLength
    max_score: MaxScore
    overtime_option: OvertimeOption
    series_length_option: SeriesLengthOption
    game_speed_option: GameSpeedOption
    ball_max_speed_option: BallMaxSpeedOption
    ball_type_option: BallTypeOption
    ball_weight_option: BallWeightOption
    ball_size_option: BallSizeOption
    ball_bounciness_option: BallBouncinessOption
    boost_option: BoostOption
    rumble_option: RumbleOption
    boost_strength_option: BoostStrengthOption
    gravity_option: GravityOption
    demolish_option: DemolishOption
    respawn_time_option: RespawnTimeOption

    def __init__(
        self,
        match_length=MatchLength(),
        max_score=MaxScore(),
        overtime_option=OvertimeOption(),
        series_length_option=SeriesLengthOption(),
        game_speed_option=GameSpeedOption(),
        ball_max_speed_option=BallMaxSpeedOption(),
        ball_type_option=BallTypeOption(),
        ball_weight_option=BallWeightOption(),
        ball_size_option=BallSizeOption(),
        ball_bounciness_option=BallBouncinessOption(),
        boost_option=BoostOption(),
        rumble_option=RumbleOption(),
        boost_strength_option=BoostStrengthOption(),
        gravity_option=GravityOption(),
        demolish_option=DemolishOption(),
        respawn_time_option=RespawnTimeOption(),
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> MutatorSettings: ...

class OvertimeOption:
    Unlimited = 0
    Five_Max_First_Score = 1
    Five_Max_Random_Team = 2

    def __init__(self, value: int = 0): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> OvertimeOption: ...

class PartyMemberBotPlayer:

    def __init__(
        self,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> PartyMemberBotPlayer: ...

class Physics:
    location: Vector3
    rotation: Rotator
    velocity: Vector3
    angular_velocity: Vector3

    def __init__(
        self,
        location=Vector3(),
        rotation=Rotator(),
        velocity=Vector3(),
        angular_velocity=Vector3(),
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> Physics: ...

class PlayerClassType(Enum):
    NONE = 0
    RLBotPlayer = 1
    HumanPlayer = 2
    PsyonixBotPlayer = 3
    PartyMemberBotPlayer = 4

class PlayerClass:
    item_type: PlayerClassType
    rlbot_player: Optional[RLBotPlayer]
    human_player: Optional[HumanPlayer]
    psyonix_bot_player: Optional[PsyonixBotPlayer]
    party_member_bot_player: Optional[PartyMemberBotPlayer]

    def __init__(
        self,
        rlbot_player=None,
        human_player=None,
        psyonix_bot_player=None,
        party_member_bot_player=None,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...

class PlayerConfiguration:
    variety: PlayerClass
    name: str
    team: int
    location: str
    run_command: str
    loadout: Optional[PlayerLoadout]
    spawn_id: int

    def __init__(
        self,
        variety=PlayerClass(),
        name="",
        team=0,
        location="",
        run_command="",
        loadout=None,
        spawn_id=0,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> PlayerConfiguration: ...

class PlayerInfo:
    physics: Physics
    score_info: ScoreInfo
    hitbox: BoxShape
    hitbox_offset: Vector3
    air_state: AirState
    dodge_timeout: float
    demolished_timeout: float
    is_supersonic: bool
    is_bot: bool
    name: str
    team: int
    boost: int
    spawn_id: int

    def __init__(
        self,
        physics=Physics(),
        score_info=ScoreInfo(),
        hitbox=BoxShape(),
        hitbox_offset=Vector3(),
        air_state=AirState(),
        dodge_timeout=0,
        demolished_timeout=0,
        is_supersonic=False,
        is_bot=False,
        name="",
        team=0,
        boost=0,
        spawn_id=0,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> PlayerInfo: ...

class PlayerInput:
    player_index: int
    controller_state: ControllerState

    def __init__(
        self,
        player_index=0,
        controller_state=ControllerState(),
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> PlayerInput: ...

class PlayerInputChange:
    player_index: int
    controller_state: ControllerState
    dodge_forward: float
    dodge_right: float

    def __init__(
        self,
        player_index=0,
        controller_state=ControllerState(),
        dodge_forward=0,
        dodge_right=0,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> PlayerInputChange: ...

class PlayerLoadout:
    team_color_id: int
    custom_color_id: int
    car_id: int
    decal_id: int
    wheels_id: int
    boost_id: int
    antenna_id: int
    hat_id: int
    paint_finish_id: int
    custom_finish_id: int
    engine_audio_id: int
    trails_id: int
    goal_explosion_id: int
    loadout_paint: Optional[LoadoutPaint]
    primary_color_lookup: Optional[Color]
    secondary_color_lookup: Optional[Color]

    def __init__(
        self,
        team_color_id=0,
        custom_color_id=0,
        car_id=0,
        decal_id=0,
        wheels_id=0,
        boost_id=0,
        antenna_id=0,
        hat_id=0,
        paint_finish_id=0,
        custom_finish_id=0,
        engine_audio_id=0,
        trails_id=0,
        goal_explosion_id=0,
        loadout_paint=None,
        primary_color_lookup=None,
        secondary_color_lookup=None,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> PlayerLoadout: ...

class PlayerSpectate:
    player_index: int

    def __init__(
        self,
        player_index=0,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> PlayerSpectate: ...

class PlayerStatEvent:
    player_index: int
    stat_type: str

    def __init__(
        self,
        player_index=0,
        stat_type="",
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> PlayerStatEvent: ...

class PolyLine3D:
    color: Color
    points: list[Vector3]

    def __init__(
        self,
        color=Color(),
        points=[],
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> PolyLine3D: ...

class PredictionSlice:
    game_seconds: float
    physics: Physics

    def __init__(
        self,
        game_seconds=0,
        physics=Physics(),
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> PredictionSlice: ...

class PsyonixBotPlayer:
    bot_skill: float

    def __init__(
        self,
        bot_skill=0,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> PsyonixBotPlayer: ...

class ReadyMessage:
    wants_ball_predictions: bool
    wants_quick_chat: bool
    wants_game_messages: bool

    def __init__(
        self,
        wants_ball_predictions=False,
        wants_quick_chat=False,
        wants_game_messages=False,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> ReadyMessage: ...

class RemoveRenderGroup:
    id: int

    def __init__(
        self,
        id=0,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> RemoveRenderGroup: ...

class RenderGroup:
    render_messages: list[RenderMessage]
    id: int

    def __init__(
        self,
        render_messages=[],
        id=0,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> RenderGroup: ...

class RenderMessage:
    variety: RenderType

    def __init__(
        self,
        variety=RenderType(),
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> RenderMessage: ...

class RenderTypeType(Enum):
    NONE = 0
    Line3D = 1
    PolyLine3D = 2
    String2D = 3
    String3D = 4

class RenderType:
    item_type: RenderTypeType
    line_3_d: Optional[Line3D]
    poly_line_3_d: Optional[PolyLine3D]
    string_2_d: Optional[String2D]
    string_3_d: Optional[String3D]

    def __init__(
        self,
        line_3_d=None,
        poly_line_3_d=None,
        string_2_d=None,
        string_3_d=None,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...

class RespawnTimeOption:
    Three_Seconds = 0
    Two_Seconds = 1
    One_Seconds = 2
    Disable_Goal_Reset = 3

    def __init__(self, value: int = 0): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> RespawnTimeOption: ...

class RLBotPlayer:

    def __init__(
        self,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> RLBotPlayer: ...

class Rotator:
    pitch: float
    yaw: float
    roll: float

    def __init__(
        self,
        pitch=0,
        yaw=0,
        roll=0,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> Rotator: ...

class RotatorPartial:
    pitch: Optional[Float]
    yaw: Optional[Float]
    roll: Optional[Float]

    def __init__(
        self,
        pitch=None,
        yaw=None,
        roll=None,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> RotatorPartial: ...

class RumbleOption:
    No_Rumble = 0
    Default = 1
    Slow = 2
    Civilized = 3
    Destruction_Derby = 4
    Spring_Loaded = 5
    Spikes_Only = 6
    Spike_Rush = 7

    def __init__(self, value: int = 0): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> RumbleOption: ...

class ScoreInfo:
    score: int
    goals: int
    own_goals: int
    assists: int
    saves: int
    shots: int
    demolitions: int

    def __init__(
        self,
        score=0,
        goals=0,
        own_goals=0,
        assists=0,
        saves=0,
        shots=0,
        demolitions=0,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> ScoreInfo: ...

class SeriesLengthOption:
    Unlimited = 0
    Three_Games = 1
    Five_Games = 2
    Seven_Games = 3

    def __init__(self, value: int = 0): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> SeriesLengthOption: ...

class SphereShape:
    diameter: float

    def __init__(
        self,
        diameter=0,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> SphereShape: ...

class StartCommand:
    config_path: str

    def __init__(
        self,
        config_path="",
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> StartCommand: ...

class String2D:
    foreground: Color
    background: Color
    scale: float
    text: str
    h_align: TextHAlign
    v_align: TextVAlign
    x: float
    y: float

    def __init__(
        self,
        foreground=Color(),
        background=Color(),
        scale=0,
        text="",
        h_align=TextHAlign(),
        v_align=TextVAlign(),
        x=0,
        y=0,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> String2D: ...

class String3D:
    foreground: Color
    background: Color
    scale: float
    text: str
    h_align: TextHAlign
    v_align: TextVAlign
    position: Vector3

    def __init__(
        self,
        foreground=Color(),
        background=Color(),
        scale=0,
        text="",
        h_align=TextHAlign(),
        v_align=TextVAlign(),
        position=Vector3(),
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> String3D: ...

class TeamInfo:
    team_index: int
    score: int

    def __init__(
        self,
        team_index=0,
        score=0,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> TeamInfo: ...

class TextHAlign:
    Left = 0
    Center = 1
    Right = 2

    def __init__(self, value: int = 0): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> TextHAlign: ...

class TextVAlign:
    Top = 0
    Center = 1
    Bottom = 2

    def __init__(self, value: int = 0): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> TextVAlign: ...

class Touch:
    player_name: str
    game_seconds: float
    location: Vector3
    normal: Vector3
    team: int
    player_index: int

    def __init__(
        self,
        player_name="",
        game_seconds=0,
        location=Vector3(),
        normal=Vector3(),
        team=0,
        player_index=0,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> Touch: ...

class Vector3:
    x: float
    y: float
    z: float

    def __init__(
        self,
        x=0,
        y=0,
        z=0,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> Vector3: ...

class Vector3Partial:
    x: Optional[Float]
    y: Optional[Float]
    z: Optional[Float]

    def __init__(
        self,
        x=None,
        y=None,
        z=None,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pack(self) -> bytes: ...
    @staticmethod
    def unpack(data: bytes) -> Vector3Partial: ...
