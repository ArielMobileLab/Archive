BoardShim.set_log_file('brainflow.log');
BoardShim.enable_dev_board_logger();
% Input the brain waves from EEG to 'params'
params = BrainFlowInputParams();
params.serial_port = 'COM4';
board_shim = BoardShim(int32(BoardIds.CYTON_DAISY_BOARD), params);
preset = int32(BrainFlowPresets.DEFAULT_PRESET);
% Prepare the board shim
board_shim.prepare_session();
board_shim.add_streamer('file://data_default.csv:w', preset);
board_shim.start_stream(45000, '');
% Define a range vector: 1-150
x=1:1:15;
% Create a graph
figure(1);hold all
for i=1:50
    % Performs a break every 0.2 seconds
    pause(0.2)
    % Entering the data from EEG to 'data'
    data = board_shim.get_current_board_data(15, preset);
    % Transpose the rows and columns
    data = transpose(data);
    %Generates a EEG plot where x-axis is a vector of 1-150 and y-axis is the
    %data of the second column from 'data'
    disp(data(:,2))
    plot(x,data(:,2));drawnow
end
% Stop the streaming of the board shim

board_shim.stop_stream();
data = board_shim.get_current_board_data(1, preset);
data = transpose(data);

% Release the board shim
board_shim.release_session();
