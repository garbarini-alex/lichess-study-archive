import backup_studies_as_pgn_files as func

"""
Lite test of general execution by running for one study
"""

study_name = 'dqCpuvFS'
study_file_name = 'dqCpuvFS_RookAndPawnEndgames.pgn'
title = 'Rook And Pawn Endgames'

func.write_to_file('manifest.csv', str(0) + ',' + str(study_name) + ',' + study_file_name + ',' + str(title) + '\n', 'a')
func.write_to_file(study_file_name, func.fetch_pgn(study_name), 'w+')
