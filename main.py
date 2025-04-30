import cv2
import time
from pyzbar.pyzbar import decode
from banco_dados import BancoDeDados

class LeitorQRCode:
    def __init__(self):
        self.banco = BancoDeDados()
        self.cap = cv2.VideoCapture(0)
        
    def ler_qr_code(self):
        print("Aproxime o QR code do crachá (Pressione '1' para sair)")
        
        try:
            while True:
                ret, frame = self.cap.read()
                if not ret:
                    break

                decoded_objects = decode(frame)
                for obj in decoded_objects:
                    id_funcionario = obj.data.decode('utf-8')
                    
                    # Verifica se é um ID válido
                    if id_funcionario.isdigit():
                        self.registrar_ponto(int(id_funcionario))
                        print(f"Ponto registrado para funcionário ID: {id_funcionario}")
                    
                    # Desenha contorno (opcional)
                    self.desenhar_contorno(frame, obj)

                cv2.imshow('Registro de Ponto', frame)
                if cv2.waitKey(1) & 0xFF == ord('1'):
                    break

        finally:
            self.banco.fechar_conexao()
            self.cap.release()
            cv2.destroyAllWindows()
    
    def registrar_ponto(self, id_funcionario):
        """Define automaticamente se é entrada ou saída"""
        # Verifica se já existe registro de entrada sem saída hoje
        self.banco.cursor.execute(
            """SELECT id FROM ponto 
            WHERE id_funcionario = ? AND data = date('now') AND hora_saida IS NULL""",
            (id_funcionario,)
        )
        
        if self.banco.cursor.fetchone():  # Se existe entrada sem saída
            self.banco.registrar_ponto(id_funcionario, 'saida')
        else:
            self.banco.registrar_ponto(id_funcionario, 'entrada')
    
    def desenhar_contorno(self, frame, obj):
        pontos = obj.polygon
        pts = [(p.x, p.y) for p in pontos]
        pts.append(pts[0])
        for i in range(len(pts)-1):
            cv2.line(frame, pts[i], pts[i+1], (0, 255, 0), 2)

if __name__ == "__main__":
    leitor = LeitorQRCode()
    leitor.ler_qr_code()