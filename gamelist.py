###
# Script by Ezechiel
# Date : 2019/05/26
# Description : PiDimBoot Gamelist
###

from const import *

GAMES_TYPES = [FIGHTING, ACTION, SPORT, HORI_SHOOTEMUP, VERT_SHOOTEMUP, PUZZLE, VARIOUS, RACING, SHOOTER]
GAMES_SYSTEMS = [ATOMISWAVE, NAOMI1, NAOMI2, CHIHIRO, TRIFORCE]


GAME_LIST = { 
    # ATOMISWAVE GAMES
    ATOMISWAVE: {         
        GAMES: {
            ACTION: {
                "Demolish Fist":                       "demolishfist.bin",
                "Dolphin Blue":                        "dol222.bin",
                "Dolphin Blue":                        "dolphinblue.bin",
                "Force Five":                          "force_five.bin",
                "Metal Slug 6":                        "mslug6.bin",
                "Kenju":                               "kenju.bin",
                "Knights of Valour Seven Spirits":     "kov7spirits.bin",
                "Knights of Valour Seven Spirits":     "kov7spirits_Naomi2_Fixed.bin"
            },
            # Fighting games
            FIGHTING: {
                "Guilty Gear X V1.5":                  "ggx15.bin",
                "Guilty Gear Isuka":                   "ggisuka_fixed.bin",
                "Fist of the North Star":              "FOTNS_Naomi2_Fixed.bin",
                "NeoGeo Battle Coliseum":              "NeoGeoBattleColliseum.bin",
                "Samurai Shodown VI":                  "SamuraiShowdownVI_SamuraiSpirits_v4.bin",
                "KOF Neowave":                         "KOFNWJapan.bin",
                "KOF 11":                              "gdrom_KOFXI_controles_JVS_OK_Video_OK_v4.bin",
                "The Rumble Fish":                     "gdrom-rumblefish.bin",
                "The Rumble Fish 2":                   "gdrom_rumblef2_v4.bin"
            },
            RACING: {
                "Faster Than Speed":                   "ftspeed.bin"
            },
            SHOOTER: {
                "Sports Shooting USA":                 "gdrom_sprtshot.bin"
            },
            SPORT: {
                "Dirty Pigskin Football":              "gdrom_dirtypigskin_v3.bin"
            },
            VARIOUS: {
                "Animal Basket":                       "gdrom_anmlbskt.bin",
                "Salary Man Kintaro":                  "gdrom_salmankt_JVS_OK_BIOS_OK_Video_OK.bin",
                "Sushi Bar":                           "gdrom_Sushibar_v2.bin"
            }
        },
    },
    #NAOMI 1 GAMES
    NAOMI1: {
        GAMES: {
            ACTION: {
                "Airline Pilot":                        "AirlinePilots.bin",
                "Cosmic Smash":                         "CosmicSmash.bin",
                "Dynamite Deka Ex":                     "DynamiteDekaEx.bin",
                "Gunspike":                             "GunSpike.bin",
                "Heavy Metal Geomatrix":               "HeavyMetalGeomatrix.bin",
                "Mob Suit Gundam Fed. Vs Zeon":        "MobileSuitGundam-FederationVsZeon.bin",
                "Mob Suit Gundam Fed. Vs Zeon DX":     "MobileSuitGundam-FederationVsZeonDX.bin",
                "Monkey Ball":                          "MonkeyBall.bin",
                "Musapeys Choco Marker":               "MusapeysChocoMarker.bin",
                "Out Triggers":                        "otrigger.bin",
                "SlashOut":                             "Slashout.bin",
                "Spawn":                                "spawn.bin",
                "Spikers Battle":                       "SpikersBattle.bin",
                "Virtual On Oratorio Tangra":          "vonot.bin",
                "Zombie Revenge":                       "ZombieRevenge.bin"
            },
            FIGHTING: {
                "Akatsuki Blitz kampf Auf Asche":      "Akatsuki_Bk_Ausf_Achse.bin",
                "Capcom vs. SNK M. Fight 2K":          "Capcom_vs_SNK_Millenium_Fight_2000.bin",
                "Capcom vs. SNK M. Fight 2K Pro":      "Capcom_vs_SNK_Millenium_Fight_2000_Pro.bin",
                "Capcom vs. SNK 2 M. Fighting 2001":   "Capcom_Vs_SNK_2_Millionaire_Fighting_2001.bin",
                "Dead or Alive 2":                      "DeadOrAlive2.bin",
                "Dead or Alive 2 Millenium":           "DeadOrAlive2Millenium.bin",
                "Giant Gram Zen. Pro Wrestle 2":       "Giant_Gram_EPR-21820_PATCHED.bin",
                "Giant Gram 2K Zn Pro Wrestle 3":      "Giant_Gram_2000.bin",
                "Guilty Gear X":                       "ggx_v2p.bin",
                "Guilty Gear XX":                       "GuiltyGearXX.bin",
                "Guilty Gear XX Reload":               "GuiltyGearXXReload.bin",
                "Guilty Gear XX Slash":                "GuiltyGearXXSlash_v6.bin",
                "Guilty Gear XX Accent Core":          "GuiltyGearXXAccentCore_v6.bin",
                "Jingy Storm The Arcade":              "JingyStormTheArcade.bin",
                "Marvel vs. Capcom 2":                 "MarvelVsCapcom2.bin",
                "Melty Blood Actress Again NP":        "MeltyBloodActressAgain.bin",
                "Melty Blood Actress Again":           "MeltyBloodActressAgain_v6.bin",
                "Melty Blood Act Cadenza [A]":         "MeltyBloodActCadenza(RevA).bin",
                "Melty Blood Act Cadenza [B]":         "MeltyBloodActCadenzaVerB_v3.bin",
                "Melty Blood Act Cadenza [B2]":        "MeltyBloodActCadenzaVerB2_v3.bin",
                "Project Justice Rival School 2":      "RivalSchools2-ProjectJustice.bin",
                "Power Stone":                          "Powerstone.bin",
                "Power Stone 2":                        "PowerStone2.bin",
                "Shin Nihon Pro Wrestling Toukon Retsuden 4 Arcade Edition":    "toukon4.bin",
                "Street Fighter Zero 3 Upper":         "StreetFighterZero3Upper.bin",
                "Toy Fighter":                          "ToyFighter.bin",
                "WWF Royal Rumble":                     "WWF_Royal_Rumble.bin"
            },
            HORI_SHOOTEMUP: {
                "Border Down":                          "BorderDown_v3.bin",
                "Chaos Field":                          "ChaosField_v3.bin",
                "Gigawing 2":                           "GigaWing2.bin",
                "Radirgy":                              "Radirgy_v3.bin", 
                "Radirgy Noa":                          "RadirgyNoa_v6.bin",
                "Senko no Ronde":                       "senkov3.bin",
                "Senko no Ronde New Ver":              "senkonewv6.bin",
                "Senko no Ronde SP":                   "SenkoNoRondeSP_v3.bin",
                "Zero Gunner 2":                        "ZeroGunner2.bin"
            },
            PUZZLE:{
                "Azumanga Daioh Puzzle Bobble":        "AzumangaDaiohPuzzleBobble_v3.bin",
                "Burning Casino":                       "BurningCasino_v3.bin",
                "Cleopatra Fortune Plus":              "CleopatraFortunePlus_v6.bin",
                "Doki Doki Idol Star Seeker":          "DokiDokiIdolStarSeeker.bin",
                "Kuru Kuru Chameleon":                 "KuruKuruChameleon_v3.bin",
                "Nomiso Kone Kone Puzzle Takoron":     "NoukonePuzzleTakoron.bin",
                "Puyo Puyo Da":                         "Puyo_Puyo_Da_EPR-22206_PATCHED.bin",
                "Puyo Puyo Fever":                      "PuyoPuyoFever_v6.bin",
                "Sega Tetris":                          "SegaTetris.bin",
                "Super Shanghai 2005":                 "SuperShanghai2005_v6.bin",
                "Super Shanghai 2005 [A]":             "SuperShanghai2005VerA_v6.bin",
                "Tetris Kiwamemichi":                  "TetrisKiwamemichi_v6.bin",
                "Usagui Yamashiro Mahjong Hen":        "Usagui_YamashiroMahjongHen_v3.bin"
            },
            RACING: {
                "18 Wheeler (STD)":                     "18_Wheeler_STD.bin",
                "18 Wheeler (DLX)":                     "18_Wheeler_DX.bin", 
                "Crazy Taxi":                           "CrazyTaxi.bin"
            },
            SHOOTER: {
                "Confidential Mission":                "ConfidentialMission.bin",
                "Death Crimson OX":                     "DeathCrimsonOX.bin",
                "Jambo Safari":                         "Jambo_Safari.bin",
                "Lupin 3 The Shooting":                "Lupin3_TheShooting.bin",
                "Maze of the King":                     "TheMazeOfTheKings.bin"
            },
            SPORT: {
                "Sports Jam":                           "SportsJam.bin",
                "Virtua Athlete":                       "VirtuaAthlete.bin",
                "Virtua Golf":                          "VirtuaGolf.bin",
                "Virtua NBA":                           "VirtuaNBA.bin",
                "Virtua Striker 2 Ver. 2000":          "VirtuaStriker2-2000.bin",
                "Virtua Tennis":                        "VirtuaTennis.bin",
                "Virtua Tennis 2":                      "VirtuaTennis2.bin",
                "Wave Runner GP":                       "WaveRunnerGP.bin",
                "World Series Baseball":               "WorldSeriesBaseball.bin"
            },
            VARIOUS:{
                "Alien Front":                          "AlienFront.bin",
                "La Keyboard xyu":                      "LaKeyboardxyu_v3.bin",
                "Lupin The Typing":                    "Lupin_TheTyping.bin",
                "Quiz Keitai Q Mode":                  "QuizKeitaiQMode.bin",
                "Samba de Amigo":                       "Samba_De_Amigo_EPR-22966B_Patched.bin",
                "Sega  Marine Fishing":                "Sega_Marine_Fishing_EPR-22221.bin",
                "Sega Strike Fighter":                 "SegaStrikeFighter.bin",
                "Typing of the Dead":                  "TheTypingOfTheDead.bin",
                "Tokyo Bus":                           "tokyobus.bin",
            },
            VERT_SHOOTEMUP: {
                "Ikaruga":                              "Ikaruga_v3.bin",
                "Illvelo":                              "Illvelo_v6.bin",
                "Karous":                               "karous_v3.bin",
                "Mamoru-kun wa Noro. Shimatta!":       "mamonorov6.bin",
                "Psyvariar 2":                          "Psyvariar2_v6.bin",
                "Shikigami no Shiro II":               "ShikigamiNoShiroII_v6.bin",
                "Shooting Love 2007 - Exzeal":         "ShootingLove2007-Exzeal_v6.bin",
                "Trigger Heart Exelica":               "TriggerHeartExelica_v6.bin",
                "Trizeal":                              "Trizeal_v3.bin",
                "Under Defeat":                         "UnderDefeat_v3.bin"
            }
        },
    },
    #NAOMI 2 GAMES
    NAOMI2: {
        GAMES: {
            # Fighting games
            FIGHTING: {
                "Virtua Fighter 4":                     "VirtuaFighter4.bin", 
                "Virtua Fighter 4 Ver. B":             "VirtuaFighter4_verb.bin",
                "Virtua Fighter 4 Ver. C":             "VirtuaFighter4_verc.bin",
                "Virtua Fighter 4 Evo":                "VirtuaFighter4Evo.bin",
                "Virtua Fighter 4 Evo Ver. B":         "VirtuaFighter4Evo_verb.bin",
                "Virtua Fighter 4 Final Tuned":        "VirtuaFighter4FinalTuned.bin",
                "Virtua Fighter 4 Final Tuned [A]":    "VirtuaFighter4FinalTuned_vera.bin",
                "Virtua Fighter 4 Final Tuned [B]":    "VirtuaFighter4FinalTuned_verb.bin"
            },
            # Racing games
            RACING: {
                "Club Kart European Session":          "ClubKartEuropeanSessionUnlocked.bin",
                "Initial D Export":                    "InitialDexp.bin",
                "Initial D  Japanese":                 "InitialDjap.bin",
                "Initial D 2 Export":                  "InitialD2exp.bin",
                "Initial D 2 Japanese":                "InitialD2jap.bin",
                "Initial D 2 Japanese [B]":            "InitialD2jap-revb.bin",
                "Initial D 3 Export":                  "Initial_D3_Export.bin",
                "King Of Route 66":                    "KingOfRoute66.bin",
                "Wild Riders":                        "wldrider.bin",
            },
            # Sport games
            SPORT: {
                "Beach Spikers":                        "BeachSpikers.bin",
                "Virtua Striker 3":                     "VirtuaStriker3.bin"
            }  
        },
    },
    #CHIHIRO GAMES
    CHIHIRO: {
        GAMES: {
            # Racing games
            RACING: {
                "Crazy Taxi High Roller":            "CrazyTaxiHighRoller.bin",
                "Out Run 2 512MB":                   "OR2_512.bin",
                "Out Run 2 1GB":                     "OR2_1gb.bin",
                "Out Run 2 BETA":                    "OR2BETA.bin",
                "Out Run 2 SP":                       "or2sp_1gb.bin",
                "Out Run 2 Spec Tours 512MB":        "Outrun_2_Special_Tours_512.bin",
                "Out Run 2 Spec Tours 1GB":          "Outrun_2_Special_Tours_1GB.bin",
                "Wangan Midnight Max Tune (EXP)":    "Wangan_Midnight_Maximum_Tune_EXPORT_(GDX-0009B).bin",
                "Wangan Midnight Max Tune 512MB":    "Wangan_Midnight_Maximum_Tune_EXP_512.bin",
                "Wangan Midnight Max Tune 1GB":      "Wangan_Midnight_Maximum_Tune_EXP_1GB.bin",
                "Wangan Midnight Max Tune 2 (JAP)":  "Wangan_Midnight_Maximum_Tune_2_JAP_(GDX-0015).bin",
                "Wangan Midnight Max Tune 2 512MB":  "Wangan_Midnight_Maximum_Tune_2_JAP_512.bin",
                "Wangan Midnight Max Tune 2 1GB":    "Wangan_Midnight_Maximum_Tune_2_JAP_1GB.bin",
                "Wangan Midnight Max Tune 2B 512M":  "Wangan_Midnight_Maximum_Tune_2B_EXP_512.bin",
                "Wangan Midnight Max Tune 2B 1GB":   "Wangan_Midnight_Maximum_Tune_2B_EXP_1GB.bin"
            },
            # Shooter games
            SHOOTER: {
                "Virtua Cop 3 512MB":                "Virtua_Cop_3_512.bin",
                "Virtua Cop 3 1GB":                  "Virtua_Cop_3_1GB.bin",
                "Ghost Squad 512M":                  "Ghost_Squad_Ver._A_512.bin",
                "Ghost Squad  1GB":                  "Ghost_Squad_Ver._A_1GB.bin",
                "The House Of The Dead 3":           "The_House_Of_The_Dead_3_GDX-0001.bin",
            },
            # Sport games
            SPORT: {
                "Sega Golf Club 2006 NT 512MB":      "Sega_Golf_Club_Version_2006_Next_Tours_Rev.A_512.bin",
                "Sega Golf Club 2006 NT 1GB":        "Sega_Golf_Club_Version_2006_Next_Tours_Rev.A_1GB.bin"
            },
            # Action games
            ACTION: {
                "Gundam Battle Operating Sim.":      "Gundam_Battle_Operating_Simulator.bin",
                "Ollie King 512MB":                  "Ollie_King_512.bin",
                "Ollie King 1GB":                    "Ollie_King_1GB.bin"
            }
        },
    },
    #TRIFORCE GAMES
    TRIFORCE: {
        GAMES: {
            RACING: {
                "F-Zero AX":                         "FZeroAx.bin",
                "Mario Kart Arcade GP":              "MarioKartGP.bin",
                "Mario Kart Arcade GP 2":            "MarioKartGP2.bin"
            },
            SPORT: {
                "Virtua Striker 2002":               "vs2002e.bin",
                "Virtua Striker 4 v2006":            "vs406.bin",
                "Virtua Striker 4 2006 (Export)":    "Virtua_Striker_4_2006_Exp.bin"
            }
        },
    }
}