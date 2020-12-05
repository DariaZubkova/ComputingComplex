function Z = globopt0(X)
% 
%   ���������� ������������ ���������� �������� ���������� �����������.
%   ������ ������ ����������� ������� �������, ������������ ���������� 
%   ������� ������� ���������� �������� ObjFunc (��. ������ 101 � ����
%   ���� ���������). ������� �����������, ������� ����� ����� ����� 
%   (�������������� ��������������� �� ���������, ������������� ���� 
%   ���������), ��������� ����� ������� ���������� X ���� '��������'. 
%  
%   ��������� � ������������� ������ � ��� ������������ ����� ���������,
%   � �������, � ������ 
%
%       Kearfott R.B. Rigorous Global Search: Continuous Problems
%         - Dordrecht: Kluwer, 1996.
%       Hansen E., Walster G.W. Global optimization using interval 
%         analysis. - New York: Marcel Dekker, 2004.
%       ����� �.�. ������������� ������������ ������. - XYZ: 2011.
%         ����������� �����, ��������� �� http://www.nsc.ru/interval
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  
  MaxStepNumber = 1000;  %   ����������� �� ���������� �������� ��������� 
  
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%   "���������������", �� ������ ������, �������� ������
%  
  X = intval(X);
    
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%  
%   ��������� ���������� ������������ �������� ���������� �����������
%  
  
%   �������������� ������� ����� ����� 
NStep = 1; 
   
%   ������� ������������ ������ ������� �������� ������� ������� 
%   �� �������� ����� X ������� ����������� 
Y = ObjFunc(X); 

UpperEst = sup(Y);  %   UpperEst - ������� ������� �������� ������� �������
                    %              �� �������� ������� ����������� X  

%   �������������� ������� ������ �������-����������, ����������
%   �������� ���� X � ������ ������� ������� ����� �� ���  
WorkList(1) = struct( 'Box', X, 'Estim', inf(Y) );
  
while ( NStep <= MaxStepNumber ) 
    
%   ������� � ������� ������ ������� ������ (������� �������������
%   ���������� ������ ������ ������� ��������), � ����� ���������� 
%   ����� Leading, � ������� (����������) ������ ���������� LeadEst 
   
    LL = size(WorkList,2);  %   ����������� ����� �������� ������
    LeadEst = UpperEst;     %   �������������� LeadEst ��������� UpperEst
    for k = 1:LL 
        p = WorkList(k).Estim;
        if p < LeadEst
            LeadEst = p;
            Leading = k; 
        end
    end
    
    %   ��� ����������� �������, ���� �����, ���������� �������� ����
    %display(NStep) 
    %display(LeadEst) 
    %display(WorkList(Leading).Box) 
    
    %   ��������� ������� �������� ����� D1 � D2,
    %   ������ �� ������� ������� �������� �����
    D1 = WorkList(Leading).Box;   D2 = D1;    
    
    %   ������� ����� ������� ���������� �������� �����
    [radmax,imax] = max(rad(D1)); 
    
    if radmax == 0
        break
    end

    %   ������ ����� ������� ���������� � D1 � D2 ������� 
    s = D1(imax); 
    D1(imax) = infsup(inf(s),mid(s)); 
    D2(imax) = infsup(mid(s),sup(s)); 
    
    %   ������� ��� ������-�������� ������������ ������ 
    %   �������� �������� ������� ������� 
    Y1 = ObjFunc(D1);   Y2 = ObjFunc(D2);  
    
    %   ��������� ������-������� Rec1 � Rec2 � �������� �� � ������� ������ 
    Rec1 = struct( 'Box', D1, 'Estim', inf(Y1) );
    Rec2 = struct( 'Box', D2, 'Estim', inf(Y2) );
    WorkList = [ WorkList  Rec1  Rec2 ];
    
    %   ������� ������ ������� ������ �� �������� ������
    WorkList(Leading) = [];  
    %   ����������� ������� ����� 
    NStep = NStep + 1;  
  
end
  
Z = WorkList; 
  
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%   ������� ������������� ���������� ������� ������� 
%
    function Y = ObjFunc(X)
    %   ������������ ������������ ���������� ������� ������� ����������
        Y = sqr(X(1)) + sqr(X(2)) - cos(18*X(1)) - cos(18*X(2));
    
    %   ������������ ������������ ���������� ������� ������� ����������
    %    Y = 101*sqr(sqr(X(1)) - X(2)) + sqr(X(1) - 1);
    
    % Matyas
    %    Y = 0.26 * (sqr(X(1)) + sqr(X(2))) - 0.48 * X(1) * X(2);
    
    % Himmelblau
    %    Y = sqr(sqr(X(1)) + X(2) - 11) + sqr(X(1) + sqr(X(2)) - 7);
        
    % Cross-in-tray function
    %   Y = -0.0001 * (abs(sin(X(1)) * sin(X(2)) * exp(abs(100 - (sqrt(sqr(X(1)) + sqr(X(2))) / pi)))) + 1) ^ 0.1;
    
    % Holder
    %   Y = -1 * (abs(sin(X(1)) * cos(X(2)) * exp(abs(1 - (sqrt(sqr(X(1)) + sqr(X(2))) / pi)))));
    
    
    % Booth
    %    Y = sqr(X(1) + 2 * X(2) - 7) - sqr(2 * X(1) + X(2) - 5);
    
    
    %   ������������ ������������ ���������� ������� ���������� �������
    %    Y = intval(0);
    %    for i = 1:5;
    %       Y = Y - i*sin((i+1)*X + i); 
    %    end
        
    end
  
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

end
  
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  